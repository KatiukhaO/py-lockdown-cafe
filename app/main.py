from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotWearingMaskError)


def go_to_cafe(friends: list, cafe: Cafe):
    no_mask = 0
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            no_mask += 1

    if no_mask:
        return f"Friends should buy {no_mask} masks"
    return f"Friends can go to {cafe.name}"
