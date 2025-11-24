from transformers import pipeline

class TriageService:
    def __init__(self):
        # O modelo facebook/bart-large-mnli é excelente para zero-shot
        print("Carregando modelo... aguarde.")
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def classify_symptom(self, text):
        # Definimos as classes possíveis (labels)
        candidate_labels = ["Emergência Médica", "Agendamento de Consulta", "Dúvida Geral", "Farmácia/Medicamentos"]
        
        # O modelo faz a mágica
        result = self.classifier(text, candidate_labels, multi_label=False)
        
        return {
            "sintoma": text,
            "categoria_sugerida": result['labels'][0],
            "confianca": f"{result['scores'][0] * 100:.2f}%"
        }