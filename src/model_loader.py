"""Simple OBJ model loader."""

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Model:
    vertices: List[Tuple[float, float, float]]
    texcoords: List[Tuple[float, float]]
    normals: List[Tuple[float, float, float]]
    faces: List[Tuple[int, int, int]]  # indices into vertices list (1-based)


def load_obj(path: str) -> Model:
    """Load a Wavefront OBJ file.

    Only vertex positions, texture coordinates, normals, and face indices are
    parsed. Faces are assumed to be triangles and indices in faces are
    1-based, following the OBJ specification.
    """
    vertices: List[Tuple[float, float, float]] = []
    texcoords: List[Tuple[float, float]] = []
    normals: List[Tuple[float, float, float]] = []
    faces: List[Tuple[int, int, int]] = []

    with open(path, 'r') as obj_file:
        for line in obj_file:
            if line.startswith('#') or not line.strip():
                continue
            prefix, *values = line.strip().split()
            if prefix == 'v':
                vertices.append(tuple(map(float, values)))
            elif prefix == 'vt':
                texcoords.append(tuple(map(float, values[:2])))
            elif prefix == 'vn':
                normals.append(tuple(map(float, values)))
            elif prefix == 'f':
                vertex_indices = []
                for group in values:
                    v, *rest = group.split('/')
                    vertex_indices.append(int(v))
                if len(vertex_indices) == 3:
                    faces.append(tuple(vertex_indices))
                else:
                    # simple fan triangulation for polygons with more than 3 vertices
                    for i in range(1, len(vertex_indices) - 1):
                        faces.append((vertex_indices[0], vertex_indices[i], vertex_indices[i+1]))
    return Model(vertices, texcoords, normals, faces)
