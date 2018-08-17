#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata

#Le quita todos los acentos y "ñ" al string "cadena" y lo retorna
def eliminaTildes(cadena):
	utf=cadena.decode('utf-8')
	s = ''.join((c for c in unicodedata.normalize('NFD',unicode(utf)) if unicodedata.category(c) != 'Mn'))
	return s.decode()



