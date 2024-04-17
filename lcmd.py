import os
import sys

fstring_man = "eval_cmd.py --model_weights {0}/Weights/best.model --vocabulary data/1m_6ex_karel/new_vocab.vocab --dataset data/1m_6ex_karel/test.json --eval_nb_ios 5 --eval_batch_size 8 --output_path {0}/Results/TestSet_ --top_k 10 --use_cuda"

dirc = sys.argv[1]

try:
    append = sys.argv[2]
except:
    append = ""


print(fstring_man.format(dirc) + ' ' + append)
os.system(fstring_man.format(dirc) + ' ' + append)
