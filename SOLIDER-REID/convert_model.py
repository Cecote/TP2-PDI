#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

import pickle as pkl
import sys
import torch

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    obj = torch.load(input_path, map_location="cpu")

    print("Chaves encontradas no arquivo:", obj.keys())

    if "teacher" in obj:
        obj = obj["teacher"]
        torch.save(obj, output_path)
        print(f"Modelo 'teacher' salvo em {output_path}")
    else:
        print("Erro: chave 'teacher' não encontrada no arquivo.")