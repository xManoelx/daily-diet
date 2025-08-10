from flask import Flask, request, jsonify
from database import init_database
from services import MealService, UserService
from utilities import validate_meal_data, validate_user_data

# Criar aplicação Flask
app = Flask(__name__)

# Inicializar banco de dados
init_database(app)

# ==================== ROTAS PRINCIPAIS ====================

# Rota para verificar se a API está funcionando
@app.route('/health')
def health():
    """Verificar se a API está funcionando"""
    return jsonify({
        'status': 'OK',
        'message': 'Daily Diet API is running!',
        'version': '1.0.0'
    })

# Rota para resetar todas as refeições do banco de dados
@app.route('/api/reset', methods=['POST'])
def reset_database():
    """Resetar banco de dados"""
    try:
        MealService.reset_all_meals()
        
        return jsonify({
            'message': 'Banco de dados resetado! Todas as refeições foram removidas.'
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao resetar banco: {str(e)}'}), 500

# ==================== ROTAS DE REFEIÇÕES ====================

# Rota para criar uma nova refeição
@app.route('/api/meals', methods=['POST'])
def create_meal():
    """Registrar uma nova refeição"""
    try:
        data = request.get_json()
        
        # Validar dados
        errors = validate_meal_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Criar refeição
        meal = MealService.create_meal(data)
        
        return jsonify({
            'message': 'Refeição registrada com sucesso!',
            'meal': meal.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

# Rota para listar todas as refeições do usuário
@app.route('/api/meals', methods=['GET'])
def list_meals():
    """Listar todas as refeições do usuário"""
    try:
        meals = MealService.get_all_meals()
        meals_list = [meal.to_dict() for meal in meals]
        
        return jsonify({
            'meals': meals_list,
            'total': len(meals_list)
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao listar refeições: {str(e)}'}), 500

# Rota para visualizar uma refeição específica pelo ID
@app.route('/api/meals/<meal_id>', methods=['GET'])
def get_meal(meal_id):
    """Visualizar uma refeição específica"""
    try:
        meal = MealService.get_meal_by_id(meal_id)
        
        if not meal:
            return jsonify({'error': 'Refeição não encontrada'}), 404
        
        return jsonify({'meal': meal.to_dict()})
        
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar refeição: {str(e)}'}), 500

# Rota para editar/atualizar uma refeição existente
@app.route('/api/meals/<meal_id>', methods=['PUT'])
def update_meal(meal_id):
    """Editar uma refeição"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        meal = MealService.update_meal(meal_id, data)
        
        if not meal:
            return jsonify({'error': 'Refeição não encontrada'}), 404
        
        return jsonify({
            'message': 'Refeição atualizada com sucesso!',
            'meal': meal.to_dict()
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar refeição: {str(e)}'}), 500

# Rota para deletar/apagar uma refeição
@app.route('/api/meals/<meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    """Apagar uma refeição"""
    try:
        success = MealService.delete_meal(meal_id)
        
        if not success:
            return jsonify({'error': 'Refeição não encontrada'}), 404
        
        return jsonify({'message': 'Refeição removida com sucesso!'})
        
    except Exception as e:
        return jsonify({'error': f'Erro ao remover refeição: {str(e)}'}), 500

# Rota para obter estatísticas das refeições (total, dentro/fora da dieta, sequências)
@app.route('/api/meals/stats', methods=['GET'])
def get_meal_stats():
    """Obter estatísticas das refeições"""
    try:
        stats = MealService.get_user_stats()
        return jsonify({'stats': stats})
        
    except Exception as e:
        return jsonify({'error': f'Erro ao obter estatísticas: {str(e)}'}), 500

# ==================== ROTAS DE USUÁRIOS ====================

# Rota para listar todos os usuários cadastrados
@app.route('/api/users', methods=['GET'])
def list_users():
    """Listar usuários"""
    try:
        users = UserService.get_all_users()
        users_list = [user.to_dict() for user in users]
        
        return jsonify({'users': users_list})
        
    except Exception as e:
        return jsonify({'error': f'Erro ao listar usuários: {str(e)}'}), 500

# Rota para buscar um usuário específico pelo ID
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Buscar usuário específico"""
    try:
        user = UserService.get_user_by_id(user_id)
        
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        return jsonify({'user': user.to_dict()})
        
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar usuário: {str(e)}'}), 500

# Rota para criar/cadastrar um novo usuário
@app.route('/api/users', methods=['POST'])
def create_user():
    """Criar novo usuário"""
    try:
        data = request.get_json()
        
        # Validar dados
        errors = validate_user_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        user = UserService.create_user(data)
        
        return jsonify({
            'message': 'Usuário criado com sucesso!',
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': f'Erro ao criar usuário: {str(e)}'}), 500

# ==================== INICIALIZAÇÃO ====================

def init_default_data():
    """Inicializar dados padrão"""
    with app.app_context():
        created, message = UserService.create_default_user()
        print(message)

if __name__ == '__main__':
    print('Iniciando Daily Diet API...')
    
    # Inicializar dados padrão
    init_default_data()
    app.run(debug=True, host='0.0.0.0', port=5000)
