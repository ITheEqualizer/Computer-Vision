import unittest
from pathlib import Path

import numpy as np
from tensorflow import keras
from tensorflow.keras.utils import img_to_array, load_img


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = REPOSITORY_ROOT / "saved_model" / "cnn_cifar10.keras"
CLASS_NAMES = (
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
)


class SavedModelContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = keras.models.load_model(MODEL_PATH)

    def predict(self, image_name):
        image = load_img(
            REPOSITORY_ROOT / image_name,
            target_size=(32, 32),
            color_mode="rgb",
        )
        image_array = img_to_array(image).astype("float32") / 255.0
        batch = np.expand_dims(image_array, axis=0)
        return self.model.predict(batch, verbose=0)[0]

    def test_model_interface(self):
        self.assertEqual(self.model.input_shape, (None, 32, 32, 3))
        self.assertEqual(self.model.output_shape, (None, len(CLASS_NAMES)))

    def test_sample_images_keep_their_expected_labels(self):
        expected_labels = {
            "img.jpg": "airplane",
            "img2.jpg": "frog",
        }

        for image_name, expected_label in expected_labels.items():
            with self.subTest(image=image_name):
                probabilities = self.predict(image_name)

                self.assertEqual(probabilities.shape, (len(CLASS_NAMES),))
                self.assertTrue(np.isfinite(probabilities).all())
                self.assertAlmostEqual(float(probabilities.sum()), 1.0, places=5)

                predicted_index = int(np.argmax(probabilities))
                self.assertEqual(CLASS_NAMES[predicted_index], expected_label)


if __name__ == "__main__":
    unittest.main()
