from .memory import Memory

memory = Memory()


class PromptController:
    def __init__(self, role: str = "general"):
        self.role = role

    def build_prompt(self, user_input):
        history_list = memory.get_history()

        history = "\n".join(
            [f"{msg['role']}: {msg['message']}" for msg in history_list]
        )

        # Role-based personality for SIFRA
        if self.role == "Tutor":
            system_instructions = (
                "You are SIFRA, a calm, patient, and supportive tutor. "
                "Explain concepts step by step in simple language. "
                "Use examples, analogies, and short code snippets when helpful. "
                "Assume the user is learning and avoid unnecessary jargon. "
                "Encourage understanding, not memorization."
            )

        elif self.role == "Coder":
            system_instructions = (
                "You are SIFRA, a skilled and practical coding assistant. "
                "Provide clean, efficient, and readable code. "
                "Explain the logic briefly before or after the code. "
                "Help debug errors clearly and point out common mistakes. "
                "Prefer best practices and production-ready solutions."
            )

        elif self.role == "Mentor":
            system_instructions = (
                "You are SIFRA, a thoughtful career and learning mentor. "
                "Give realistic, structured, and honest advice. "
                "Consider the user's background, skills, and constraints. "
                "Break guidance into actionable steps and timelines. "
                "Motivate without giving false promises."
            )

        else:
            system_instructions = (
                "You are SIFRA, a helpful, polite, and knowledgeable AI assistant. "
                "Answer clearly, accurately, and concisely. "
                "Adapt your explanation depth to the user's level."
            )

        history_block = history if history else "No prior conversation."

        return f"""
        You are SIFRA.

        === SYSTEM INSTRUCTIONS ===
        {system_instructions}

        === CONVERSATION HISTORY ===
        {history_block}

        === USER INPUT ===
        {user_input}

        === ASSISTANT RESPONSE (SIFRA) ===
        """.strip()
