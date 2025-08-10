from database import db
from datetime import datetime

class MealService:
    """Serviços para gerenciar refeições"""
    
    @staticmethod
    def create_meal(data, user_id='user-1'):
        """Criar uma nova refeição"""
        from models import Meal  # Importação local para evitar circular import
        
        meal = Meal(
            name=data['name'],
            description=data.get('description', ''),
            date_time=datetime.fromisoformat(data['date_time'].replace('Z', '+00:00')),
            is_on_diet=data['is_on_diet'],
            user_id=user_id
        )
        
        db.session.add(meal)
        db.session.commit()
        return meal
    
    @staticmethod
    def get_all_meals(user_id='user-1'):
        """Listar todas as refeições do usuário"""
        from models import Meal
        return Meal.query.filter_by(user_id=user_id).order_by(Meal.date_time.desc()).all()
    
    @staticmethod
    def get_meal_by_id(meal_id, user_id='user-1'):
        """Buscar uma refeição específica"""
        from models import Meal
        return Meal.query.filter_by(id=meal_id, user_id=user_id).first()
    
    @staticmethod
    def update_meal(meal_id, data, user_id='user-1'):
        """Atualizar uma refeição"""
        from models import Meal
        
        meal = Meal.query.filter_by(id=meal_id, user_id=user_id).first()
        
        if not meal:
            return None
        
        # Atualizar campos fornecidos
        if 'name' in data:
            meal.name = data['name']
        if 'description' in data:
            meal.description = data['description']
        if 'date_time' in data:
            meal.date_time = datetime.fromisoformat(data['date_time'].replace('Z', '+00:00'))
        if 'is_on_diet' in data:
            meal.is_on_diet = data['is_on_diet']
        
        meal.updated_at = datetime.utcnow()
        db.session.commit()
        return meal
    
    @staticmethod
    def delete_meal(meal_id, user_id='user-1'):
        """Deletar uma refeição"""
        from models import Meal
        
        meal = Meal.query.filter_by(id=meal_id, user_id=user_id).first()
        
        if not meal:
            return False
        
        db.session.delete(meal)
        db.session.commit()
        return True
    
    @staticmethod
    def get_user_stats(user_id='user-1'):
        """Obter estatísticas do usuário"""
        from models import Meal
        
        # Total de refeições
        total_meals = Meal.query.filter_by(user_id=user_id).count()
        
        # Refeições dentro da dieta
        meals_on_diet = Meal.query.filter_by(user_id=user_id, is_on_diet=True).count()
        
        # Refeições fora da dieta
        meals_off_diet = total_meals - meals_on_diet
        
        # Percentual na dieta
        diet_percentage = (meals_on_diet / total_meals * 100) if total_meals > 0 else 0
        
        # Melhor sequência de refeições na dieta
        meals = Meal.query.filter_by(user_id=user_id).order_by(Meal.date_time.asc()).all()
        
        current_streak = 0
        best_streak = 0
        
        for meal in meals:
            if meal.is_on_diet:
                current_streak += 1
                best_streak = max(best_streak, current_streak)
            else:
                current_streak = 0
        
        return {
            'total_meals': total_meals,
            'meals_on_diet': meals_on_diet,
            'meals_off_diet': meals_off_diet,
            'diet_percentage': round(diet_percentage, 2),
            'best_diet_streak': best_streak,
            'current_streak': current_streak
        }
    
    @staticmethod
    def reset_all_meals():
        """Resetar todas as refeições"""
        from models import Meal
        Meal.query.delete()
        db.session.commit()

class UserService:
    """Serviços para gerenciar usuários"""
    
    @staticmethod
    def get_all_users():
        """Listar todos os usuários"""
        from models import User
        return User.query.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        """Buscar usuário por ID"""
        from models import User
        return User.query.filter_by(id=user_id).first()
    
    @staticmethod
    def create_user(data):
        """Criar um novo usuário"""
        from models import User
        
        user = User(
            name=data['name'],
            email=data['email']
        )
        
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def create_default_user():
        """Criar usuário padrão se não existir"""
        from models import User
        
        user = User.query.filter_by(id='user-1').first()
        
        if not user:
            user = User(
                id='user-1',
                name='Usuário de Teste',
                email='teste@dailydiet.com'
            )
            db.session.add(user)
            db.session.commit()
            return True, 'Usuário padrão criado'
        
        return False, 'Usuário padrão já existe' 
    
        # Total de refeições
        total_meals = Meal.query.filter_by(user_id=user_id).count()
        
        # Refeições dentro da dieta
        meals_on_diet = Meal.query.filter_by(user_id=user_id, is_on_diet=True).count()
        
        # Refeições fora da dieta
        meals_off_diet = total_meals - meals_on_diet
        
        # Percentual na dieta
        diet_percentage = (meals_on_diet / total_meals * 100) if total_meals > 0 else 0
        
        # Melhor sequência de refeições na dieta
        meals = Meal.query.filter_by(user_id=user_id).order_by(Meal.date_time.asc()).all()
        
        current_streak = 0
        best_streak = 0
        
        for meal in meals:
            if meal.is_on_diet:
                current_streak += 1
                best_streak = max(best_streak, current_streak)
            else:
                current_streak = 0
        
        return {
            'total_meals': total_meals,
            'meals_on_diet': meals_on_diet,
            'meals_off_diet': meals_off_diet,
            'diet_percentage': round(diet_percentage, 2),
            'best_diet_streak': best_streak,
            'current_streak': current_streak
        }
    
    @staticmethod
    def reset_all_meals():
        """Resetar todas as refeições"""
        Meal.query.delete()
        db.session.commit()

class UserService:
    """Serviços para gerenciar usuários"""
    
    @staticmethod
    def get_all_users():
        """Listar todos os usuários"""
        return User.query.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        """Buscar usuário por ID"""
        return User.query.filter_by(id=user_id).first()
    
    @staticmethod
    def create_user(data):
        """Criar um novo usuário"""
        user = User(
            name=data['name'],
            email=data['email']
        )
        
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def create_default_user():
        """Criar usuário padrão se não existir"""
        user = User.query.filter_by(id='user-1').first()
        
        if not user:
            user = User(
                id='user-1',
                name='Usuário de Teste',
                email='teste@dailydiet.com'
            )
            db.session.add(user)
            db.session.commit()
            return True, 'Usuário padrão criado'
        
        return False, 'Usuário padrão já existe'