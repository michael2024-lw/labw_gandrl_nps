import os
import shutil


batch = [1,2,4,8]

inner_batch = [1,2,4,8]

beam_size = [8,16]


params = []
for p1 in reversed(beam_size):
    for p2 in reversed(inner_batch):
        for p3 in reversed(batch):
            params.append((p3,p2,p1))

fstring = "train_cmd.py  --signal beam_rl  --environment BlackBoxGeneralization  --reward_comb RenormExpected  --rl_inner_batch {1}  --rl_use_ref  --rl_beam {2}  --init_weights exps3man/supervised_use_grammar/Weights/best.model  --nb_epochs 5  --optim_alg Adam  --learning_rate 1e-5  --batch_size {0}  --train_file tune/data3man_{0}_{1}_{2}/1m_6ex_karel/train.json  --val_file tune/data3man_{0}_{1}_{2}/1m_6ex_karel/val.json  --vocab tune/data3man_{0}_{1}_{2}/1m_6ex_karel/new_vocab.vocab  --result_folder tune/data3man_{0}_{1}_{2}/beamrl_finetune  --use_grammar  --use_cuda"
fdir = "tune/data3man_{0}_{1}_{2}"
flog = "tune/data3man_{0}_{1}_{2}/log_{0}_{1}_{2}.txt"


with open("cmd.txt", 'w') as f:
    for p1,p2,p3 in params:
        f.write(fstring.format(p1,p2,p3) + " &> "+flog.format(p1,p2,p3)+" ; ")
        if not os.path.exists(fdir.format(p1,p2,p3)):
            shutil.copytree('data3man', fdir.format(p1,p2,p3))
            print(fdir.format(p1,p2,p3))

