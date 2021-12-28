from hanoi import Pilar, move_disk, move_tower, get_pilars
from stack import Stack
import pytest

def test_pilar_type_is_Stack():
    assert isinstance(Pilar(3), Stack)

def test_start_pilar_has_n_disks():
    p = Pilar(3)
    assert not p.is_empty()
    assert p.pop() == 1
    assert p.pop() == 2
    assert p.pop() == 3

def test_pilar_compare_nums_before_push():
    p = Pilar(3, start_pilar=False)
    p.push(1)
    with pytest.raises(Pilar.NewDiskIsGreaterThanLastDisk):
        p.push(3)

def test_move_disk():
    p1 = Pilar(3)
    p2 = Pilar(3, start_pilar=False)
    pilars = [p1, p2]
    move_disk(0, 1, pilars)
    assert pilars[0].peek() == 2
    assert pilars[1].peek() == 1

def test_move_tower_fill_to_pilar():
    pilars = get_pilars(n_pilar=3, n_disk=3)
    move_tower(n_disk=3, from_p=0, to_p=2, pilars=pilars)
    assert pilars[0].is_empty()
    assert pilars[1].is_empty()
    assert pilars[2].peek() == 1
    assert len(pilars[2]) == 3