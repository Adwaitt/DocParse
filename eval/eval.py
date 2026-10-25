def edit_distance(s1: str, s2: str) -> int:
    """Counts character differences (insertions, deletions, substitutions)."""
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1): dp[i][0] = i
    for j in range(len(s2) + 1): dp[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost # substitution
            )
    return dp[-1][-1]

def evaluate_ocr(gt: dict, pred: dict) -> dict:
    correct_fields = 0
    total_edits = 0
    total_chars = 0

    for key, gt_val in gt.items():
        # Clean both strings (strip extra spaces and match case)
        gt_clean = str(gt_val).strip().upper()
        pred_clean = str(pred.get(key, "")).strip().upper()

        # 1. Exact field match
        if gt_clean == pred_clean:
            correct_fields += 1

        # 2. Accumulate character mistakes
        total_edits += edit_distance(gt_clean, pred_clean)
        total_chars += len(gt_clean)

    # Compute overall metrics
    field_acc = correct_fields / len(gt) if gt else 0.0
    cer = total_edits / total_chars if total_chars else 0.0

    return round(field_acc, 2),  round(cer, 2)