if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path

        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from create_chart import create_double_bars
    else:
        from ..create_chart import create_double_bars

genres = ["a", "b", "c", "d", "e", "f", "g"]
tickets = [500, 1000, 1500, 2000, 3000, 2000, 2000]
sales = [1000, 2000, 3000, 4000, 6000, 2000, 1000]
sale_shr = [50, 60, 70, 80, 90, 150, 100]
open_cnt = [100, 200, 300, 500, 400, 150, 500]
run_cnt = [100, 200, 400, 300, 200, 150, 100]
aud_shr = [400, 300, 500, 400, 100, 500, 400]


create_double_bars("X Label", "Y Label", genres, tickets=tickets, sales=sales)
create_double_bars("X Label", "Y Label", genres, open_count=open_cnt, run_count=run_cnt)
create_double_bars(
    "X Label", "Y Label", genres, sale_share=sale_shr, audience_share=aud_shr
)
