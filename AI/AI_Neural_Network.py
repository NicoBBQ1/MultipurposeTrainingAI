import tensorflow as tf
from tensorflow.keras import layers, models

class AINeuralNetwork:
    def __init__(self, input_shape=(28, 28), num_classes=10):
        self.model = self.build_model(input_shape, num_classes)

    def build_model(self, input_shape, num_classes):
        model = models.Sequential([
            layers.Flatten(input_shape=input_shape),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.2),
            layers.Dense(num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train_model(self, train_images, train_labels, test_images, test_labels, epochs=5):
        self.model.fit(train_images, train_labels, epochs=epochs, validation_data=(test_images, test_labels))

    def evaluate_model(self, test_images, test_labels):
        test_loss, test_acc = self.model.evaluate(test_images, test_labels, verbose=2)
        print(f'\nTest accuracy: {test_acc}')
