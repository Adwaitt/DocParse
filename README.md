# DocParse
This repo contains the .ipynb notebooks, the comparison table of different projects, the data used, the outputs from both the methods and evaluation script used. For fixed layout data, PAN card scans have been used whereas for variable layout data UDYAM certificate scans have been used. All benchmarks were conducted on a T4 GPUs provided by kaggle.

## Qwen-2.5-VL-7B-Instruct

### Evaluation
1. **field-level accuracy** for PAN card scans: **97.5%**
2. **character error rate** for PAN card scans: **0.1%**
3. **field-level accuracy** for UDYAM certificate scans: **100%**
4. **character error rate** for UDYAM certificate scans: **1.0%**

### Latency
It takes about 14 seconds per sample for fixed layout scans and 20.3 seconds per sample for variable layout scans.

### Cost per thousand samples
On an average it can take about 5 hours for processing to happen. Assuming the system draws 170W and the rate is 8 rupees per Kwh it will cost around 6.25 rupees for processing 1000 samples.

## Paddle-OCR

### Evaluation
1. **field-level accuracy** for PAN card scans: **82.5%**
2. **character error rate** for PAN card scans: **2.7%**
3. **field-level accuracy** for UDYAM certificate scans: **85%**
4. **character error rate** for UDYAM certificate scans: **10.5%**

### Latency
It takes about 3.15 seconds per sample for fixed layout scans and 4.11 seconds per sample for variable layout scans.

### Cost per thousand samples
On an average it can take about 3600 seconds for processing to happen. Assuming the system draws 170W and the rate is 8 rupees per Kwh it will cost about 1.25 rupees for processing 1000 samples.
