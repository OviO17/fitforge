from .services import get_rank_badge_path, get_rank_for_points, get_total_points


def current_rank(request):
    if not request.user.is_authenticated:
        return {}

    points = get_total_points(request.user)
    rank_name = get_rank_for_points(points)
    return {
        'global_points': points,
        'global_rank': rank_name,
        'global_rank_badge_path': get_rank_badge_path(rank_name),
    }
