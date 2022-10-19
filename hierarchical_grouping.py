# Python
from math import sqrt
from typing import Dict, Tuple, List
from random import randint


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def get_coordinates(self) -> Tuple[int, int]:
        return (self.x, self.y)
        

def generate_points(amount: int) -> Dict[str, Vector]:
    vectors: Dict[str, Vector] = {}
    
    for i in range(amount):
        vectors[f'p{str(i)}'] = Vector(randint(0, 10), randint(0, 10))
    
    return vectors


def get_distances(vectors: Dict[str, Vector],
                  distances: Dict[str, float]) -> Dict[str, float]:
    for key, value in vectors.items():
        for key_aux, value_aux in vectors.items():
            if key == key_aux:
                continue
            
            try:
                distances[f'{key}*{key_aux}']
                
            except KeyError:
                try:
                    distances[f'{key_aux}*{key}']
                    
                except KeyError:
                    distance: float = calculate_distance(value, value_aux)
                    distances[f'{key}*{key_aux}'] = distance
    
    return distances


def calculate_distance(vector_1: Vector, vector_2: Vector) -> float:
    a, b = vector_1.get_coordinates()
    c, d = vector_2.get_coordinates()
    
    return sqrt((a - c)**2 + (b - d)**2)


def group_the_vectors(vectors: Dict[str, Vector], distances: Dict[str, float]):
    show_vectors(vectors)
    
    if len(vectors) > 1:
        distances = get_distances(vectors, distances)
        
        vectors_min_distance: List[str] = find_min_distance(distances).split('*')
        vector_1, vector_2 = vectors_min_distance
        
        mid_vector: Vector = find_mid_vector(vectors[vector_1], vectors[vector_2])
        vectors[f'{vector_1}-{vector_2}'] = mid_vector
        
        vectors.pop(vector_1)
        vectors.pop(vector_2)
        distances = {key: value for key, value in distances.items() 
                     if f'*{vector_1}' not in key 
                     if f'{vector_1}*' not in key
                     if f'*{vector_2}' not in key 
                     if f'{vector_2}*' not in key}
        
        group_the_vectors(vectors, distances)


def find_min_distance(distances: Dict[str, float]) -> str:
    distance_keys: List[str] = list(distances.keys())
    distance_values: List[str] = list(distances.values())
    
    return distance_keys[distance_values.index(min(distance_values))]


def find_mid_vector(vector_1: Vector, vector_2: Vector) -> Vector:
    a, b = vector_1.get_coordinates()
    c, d = vector_2.get_coordinates()
    x: float = (a + c) / 2
    y: float = (b + d) / 2
    
    return Vector(x, y)


def show_vectors(vectors: Dict[str, Vector]):
    print('---------------------------------------------')
    for key, value in vectors.items():
        print(f'{key} -> {value.get_coordinates()}')


def test_run():
    TEST_POINTS_1 = {
                    'p0': Vector(23, 96), 
                    'p1': Vector(30, 73),
                    'p2': Vector(71, 6),
                    'p3': Vector(33, 67),
                    'p4': Vector(78, 96),
                    'p5': Vector(83, 82),
                    'p6': Vector(85, 51)
                   }
    TEST_POINTS_2 = {
                    'p0': Vector(2, 2), 
                    'p1': Vector(4, 5),
                    'p2': Vector(1, 5),
                    'p3': Vector(0, 2),
                    'p4': Vector(2, 6),
                    'p5': Vector(0, 0),
                    'p6': Vector(1, 6), 
                    'p7': Vector(4, 8)
                   }
    
    # group_the_vectors(TEST_POINTS_1, {})
    group_the_vectors(TEST_POINTS_2, {})


def run():
    number_of_points: int = 10
    distance_points: Dict[str, float] = {}
    
    points = generate_points(number_of_points)
    group_the_vectors(points, distance_points)


if __name__ == '__main__':
    run()
    # test_run()