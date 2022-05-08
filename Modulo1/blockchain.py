#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 09:34:18 2022

@author: jaumecarreras
"""

# Modulo 1 Crear una cadena de bloques
# Flask==0.12.2: pip install Flask==0.12.2
#Cliente HTTP Postman: https://getpostman.com/

# importar librerias

import datetime
import hashlib
import json
from flask import Flask, jsonify

# Parte 1 - crear cadena de blouqes

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain)+1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash}    
        self.chain.append(block)
        return block
    
                 
            
            