import numpy
from pandas import DataFrame, Series


def points():
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympics_count_df = DataFrame({
        'country_name': Series(countries),
        'gold': Series(gold),
        'silver': Series(silver),
        'bronze': Series(bronze)
    })
    olympics_count = olympics_count_df[['gold', 'silver', 'bronze']]
    points = numpy.dot(olympics_count, [4, 2, 1])
    olympic_points = {
        'country_name': Series(countries),
        'points': Series(points)
    }
    olympic_points_df = DataFrame(olympic_points)
    return olympic_points_df

if __name__ == '__main__':
    print(points())