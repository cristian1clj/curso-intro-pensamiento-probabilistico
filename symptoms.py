
def bayes_calculate(prob_A: float, prob_b_a: float, prob_b: float) -> float:
    return (prob_A * prob_b_a) / prob_b


def run():
    cancer_prob: float = 1 / 100000
    no_cancer_prob: float = 1 - cancer_prob
    symptom_if_cancer_prob: float = 1 / 1
    symptom_if_no_cancer_prob: float = 10 / 99999
    
    symptom_prob: float = (cancer_prob * symptom_if_cancer_prob) + (no_cancer_prob * symptom_if_no_cancer_prob)

    cancer_for_symptom_prob: float = bayes_calculate(cancer_prob, symptom_if_cancer_prob, symptom_prob)
    print(cancer_for_symptom_prob)
    

if __name__ == '__main__':
    run()