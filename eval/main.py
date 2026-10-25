import json
import glob
import pandas as pd
from eval import evaluate_ocr

def main():
    f_paddle = glob.glob('../paddle_ocr/output/fixed_layout/*.json')
    f_gt = glob.glob('../data/fixed_layout/gt/*.json')
    f_qwen = glob.glob('../qwen/output/fixed_layout/*.json')
    v_paddle = glob.glob('../paddle_ocr/output/variable_layout/*.json')
    v_gt = glob.glob('../data/variable_layout/gt/*.json')
    v_qwen = glob.glob('../qwen/output/variable_layout/*.json')
    fix_data = []
    var_data = []
    for i in range(len(f_gt)):
        f_name = f_gt[i].split('/')[-1].replace('json', 'png')
        v_name = v_gt[i].split('/')[-1].replace('json', 'png')
        pffa, pfcer = evaluate_ocr(json.load(open(f_gt[i])), json.load(open(f_paddle[i]))) 
        pvfa, pvcer = evaluate_ocr(json.load(open(v_gt[i])), json.load(open(v_paddle[i])))
        qffa, qfcer = evaluate_ocr(json.load(open(f_gt[i])), json.load(open(f_qwen[i])))
        qvfa, qvcer = evaluate_ocr(json.load(open(v_gt[i])), json.load(open(v_qwen[i])))
        fix_data.append((f_name, pffa, pfcer, qffa, qfcer))
        var_data.append((v_name, pvfa, pvcer, qvfa, qvcer))
    fdf = pd.DataFrame(columns = ['filename', 'paddle_field_acc', 'paddle_cer', 'qwen_field_acc', 'qwen_cer'], data = fix_data)
    fdf.to_csv('fixed.csv', index = False)
    vdf = pd.DataFrame(columns = ['filename', 'paddle_field_acc', 'paddle_cer', 'qwen_field_acc', 'qwen_cer'], data = var_data)
    vdf.to_csv('variable.csv',  index = False)

if __name__ == "__main__":
    main()
