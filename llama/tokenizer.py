# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

import os
from logging import getLogger
from typing import List

from sentencepiece import SentencePieceProcessor


logger = getLogger()


class Tokenizer:
    """
    A class used to handle tokenization tasks using SentencePiece model.
    
    Attributes:
        sp_model (SentencePieceProcessor): The SentencePiece model used for tokenization.
        n_words (int): The number of words in the vocabulary.
        bos_id (int): The ID for the beginning of sentence token.
        eos_id (int): The ID for the end of sentence token.
        pad_id (int): The ID for the padding token.
    
    Methods:
        encode(s: str, bos: bool, eos: bool) -> List[int]:
            Encodes a string into a list of integers representing tokens.
        decode(t: List[int]) -> str:
            Decodes a list of integers representing tokens back into a string.
    """
    def __init__(self, model_path: str):
        """
        Initializes the Tokenizer class by loading the SentencePiece model and setting up the token IDs.
        Asserts that the model file exists and that the vocabulary size matches the piece size.
        """
        # reload tokenizer
        assert os.path.isfile(model_path), model_path
        self.sp_model = SentencePieceProcessor(model_file=model_path)
        logger.info(f"Reloaded SentencePiece model from {model_path}")

        # BOS / EOS token IDs
        self.n_words: int = self.sp_model.vocab_size()
        self.bos_id: int = self.sp_model.bos_id()
        self.eos_id: int = self.sp_model.eos_id()
        self.pad_id: int = self.sp_model.pad_id()
        logger.info(
            f"#words: {self.n_words} - BOS ID: {self.bos_id} - EOS ID: {self.eos_id}"
        )
        assert self.sp_model.vocab_size() == self.sp_model.get_piece_size()

    def encode(self, s: str, bos: bool, eos: bool) -> List[int]:
        """
        Encodes a string into a list of integers representing tokens.
        If `bos` is True, a beginning of sentence token is added at the start.
        If `eos` is True, an end of sentence token is added at the end.
        Asserts that the input is a string.
        """
        assert type(s) is str
        t = self.sp_model.encode(s)
        if bos:
            t = [self.bos_id] + t
        if eos:
            t = t + [self.eos_id]
        return t

    def decode(self, t: List[int]) -> str:
        """
        Decodes a list of integers representing tokens back into a string.
        """
        return self.sp_model.decode(t)
