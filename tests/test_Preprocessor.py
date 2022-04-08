import unittest
from src.data_preparation.Preprocessor import Preprocessor
import pandas as pd


class PreprocessorMethods(unittest.TestCase):
    
    preprocessor = Preprocessor(stopwords_file_path = "E:\coding\pythonnew\intel\HSProject\src\data_preparation\polish_stopwords.txt")
    dataset = pd.DataFrame({
            'Text':["""Ostatnie wypowiedzi Rosji są jasne.
                        Kreml wprost mówi- dokonujemy ludobójstwa, będziemy robić to dalej.
                        Bruksela? "Nie przesadzajmy z sankcjami".
                        Jeśli ktoś myślał, że trupy z Buczy coś zmienią- mylił się.
                        Powtórzę. Dzisiejsza UE, pod przewodnictwem Berlina, NIE MA już racji bytu """, 'nick', 'krish', 'jack'],
            'Age':[20, 21, 19, 18]}
        )
    def test_fit(self):
        
        self.preprocessor.fit(self.dataset)
        # self.assertIsNotNone(self.preprocessor.dataset)
        self.assertIsInstance(self.preprocessor.dataset, pd.DataFrame)

    # need implementation, the one below is just a sample
    def test_transform(self):

        self.preprocessor.fit(self.dataset)
        self.preprocessor.transform(["Text"])
        self.assertIsInstance(self.preprocessor.dataset, pd.DataFrame)
        self.assertIsNotNone(self.preprocessor.dataset)
    
