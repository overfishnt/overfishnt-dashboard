import os
from dataclasses import dataclass

import tensorflow as tf
from tensorflow import keras
from data_transformation import DataTransformation


class Callback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs = {}):
        if logs.get('accuracy') is not None and logs.get('accuracy') > 0.99:
            print("\nReached 99% accuracy so cancelling training!!")
            self.model.stop_training = True

class Predictions:
    def __init__(
        self, 
        data_import: str,
        buffer_size: int = 1000,
        batch_size: int = 32,
        learning_rate: float = 1e-3,
        epochs = 10
    ):
        self._data = data_import
        self._buffer_size = buffer_size
        self._batch_size = batch_size
        self._learning_rate = learning_rate
        self._epochs = epochs

        self._build_model()
        self.X_train, self.y_train, self.X_val, self.y_val, self.train, self.val, self.test, self.j = DataTransformation._data_splitting()

    def _build_model(self, unit_1: int, unit_2: int):
        tf.keras.backend.clear_session()
        n_timesteps, n_features, n_outputs = self.X_train.shape[1], self.X_train.shape[2], self.y_train.shape[1]
        self._model = tf.keras.models.Sequential([
            tf.keras.layers.LSTM(unit_1, activation='relu', input_shape=(n_timesteps, n_features)),
            tf.keras.layers.Dense(unit_2, activation='relu'),
            tf.keras.layers.Dense(unit_2, activation='relu'),
            tf.keras.layers.Dense(unit_2, activation='relu'),
            tf.keras.layers.Dense(unit_2, activation='relu'),
            tf.keras.layers.Dense(n_outputs),
        ])

        self._model.compile(
            loss = keras.losses.MeanSquaredError(),
            optimizer = keras.optimizers.Adam(learning_rate = self._learning_rate),
            metrics = ["accuracy"]
        )

        return self._model

