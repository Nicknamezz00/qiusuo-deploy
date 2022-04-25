from backend.permissions import PerformActionPermission


class CommentPermission(PerformActionPermission):
    """
    校验JWT表明的身份与相关对象拥有者身份
    """
