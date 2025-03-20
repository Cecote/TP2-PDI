CUDA_VISIBLE_DEVICES=0 python3 train.py --config_file configs/market/swin_small.yml MODEL.PRETRAIN_CHOICE 'self' MODEL.PRETRAIN_PATH '/home/cecode/Documentos/IUST/IUST_PersonReId-main/SOLIDER-REID/swin_small.pth' SOLVER.BASE_LR 0.0002 SOLVER.OPTIMIZER_NAME 'SGD' MODEL.SEMANTIC_WEIGHT 0.2


