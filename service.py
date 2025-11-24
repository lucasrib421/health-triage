from transformers import pipeline

class TriageService:
    def __init__(self):
        print("Carregando modelo multilíngue... aguarde.")
        # O modelo abaixo é MUITO melhor para português
        self.classifier = pipeline(
            "zero-shot-classification", 
            model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
        )

    def classify_symptom(self, text):
        # Labels mais descritivas ajudam o modelo a entender o contexto
        candidate_labels = [
            "Emergência Médica Grave (Risco de Vida)",
            "Agendamento de Consulta Eletiva",
            "Dúvidas Administrativas ou Gerais",
            "Compra de Medicamentos ou Farmácia"
        ]
        
        # Hipótese em português (O Pulo do Gato!)
        # Por padrão ele usa "This example is...". Vamos forçar o português.
        result = self.classifier(
            text, 
            candidate_labels, 
            multi_label=False,
            hypothesis_template="Este texto é sobre {}."
        )
        
        return {
            "sintoma": text,
            "categoria_sugerida": result['labels'][0],
            "confianca": f"{result['scores'][0] * 100:.2f}%"
        }