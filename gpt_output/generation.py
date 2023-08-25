start
class Message:
    """
    A TypedDict representing a message in a dialogue. It contains the role of the sender and the content of the message.
    """

class CompletionPrediction:
    """
    A TypedDict representing a text completion prediction. It contains the generated text, and optionally the tokens
    and log probabilities of the tokens.
    """

class ChatPrediction:
    """
    A TypedDict representing a chat prediction. It contains the generated message, and optionally the tokens and log
    probabilities of the tokens.
    """

class Llama:
    """
    The main class for the Llama 2 language model. It provides methods for building the model, generating text, and
    performing text completion and chat completion tasks.
    """

    def build():
        """
        A static method that builds a Llama model. It initializes the model parallel and loads the model weights from
        the checkpoint directory. It also initializes the tokenizer.
        """

    def __init__():
        """
        Initializes a Llama instance with a Transformer model and a tokenizer.
        """

    def generate():
        """
        Generates text given a list of prompt tokens. It also supports controlling the generation process with
        temperature and top_p parameters, and can return log probabilities of the generated tokens.
        """

    def text_completion():
        """
        Performs text completion tasks given a list of prompts. It generates text that completes the prompts and returns
        a list of CompletionPrediction instances.
        """

    def chat_completion():
        """
        Performs chat completion tasks given a list of dialogs. It generates responses to the dialogs and returns a
        list of ChatPrediction instances.
        """
end
start
def sample_top_p(probs, p):
    """
    This function performs top-p sampling from the provided probabilities.

    Args:
        probs (torch.Tensor): The probabilities from which to sample. The tensor should have the same
            shape as the output of the model's forward method.
        p (float): The cumulative probability threshold. Only tokens with a cumulative probability less
            than this value will be considered in the sampling process.

    Returns:
        next_token (torch.Tensor): The sampled token indices. The tensor has the same shape as the input
            probabilities tensor, but with the last dimension reduced to 1.
    """
end
