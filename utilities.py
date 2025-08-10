from datetime import datetime

def validate_meal_data(data):
    """Validar dados de refeição"""
    errors = []
    
    if not data:
        errors.append('Dados não fornecidos')
        return errors
    
    if not data.get('name'):
        errors.append('Nome da refeição é obrigatório')
    
    if not data.get('date_time'):
        errors.append('Data e hora são obrigatórias')
    else:
        try:
            datetime.fromisoformat(data['date_time'].replace('Z', '+00:00'))
        except ValueError:
            errors.append('Formato de data inválido')
    
    if 'is_on_diet' not in data:
        errors.append('Campo is_on_diet é obrigatório')
    elif not isinstance(data['is_on_diet'], bool):
        errors.append('Campo is_on_diet deve ser verdadeiro ou falso')
    
    return errors

def validate_user_data(data):
    """Validar dados de usuário"""
    errors = []
    
    if not data:
        errors.append('Dados não fornecidos')
        return errors
    
    if not data.get('name'):
        errors.append('Nome é obrigatório')
    
    if not data.get('email'):
        errors.append('Email é obrigatório')
    
    return errors