import numpy as np

def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute the average hinge loss for SVM classification.
    
    Args:
        y_true: Array of true labels (-1 or +1)
        y_pred: Array of predicted scores (raw SVM scores)
    
    Returns:
        Average hinge loss rounded to 4 decimal places
    """

    shape = y_pred.shape[0]
    result = np.maximum(np.zeros(shape) ,np.ones(shape) - (y_true*y_pred))

    return np.mean(result)
    