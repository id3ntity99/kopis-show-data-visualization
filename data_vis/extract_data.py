def extract_day_data(data):
    data = data["prfsts"]["prfst"]
    data_length = len(data)
    date = [data[i]["prfdt"] for i in range(data_length)]
    open_cnt = [data[i]["prfprocnt"] for i in range(data_length)]
    run_cnt = [data[i]["prfdtcnt"] for i in range(data_length)]
    sales = [data[i]["amount"] for i in range(data_length)]
    tickets = [data[i]["nmrs"] for i in range(data_length)]

    return date, open_cnt, run_cnt, sales, tickets


def extract_genre_data(data):
    data = data["prfsts"]["prfst"]
    data_length = len(data)
    genres = [data[i]["cate"] for i in range(data_length)]
    tickets = [data[i]["nmrs"] for i in range(data_length)]
    sales = [data[i]["amount"] for i in range(data_length)]
    sale_shr = [data[i]["amountshr"] for i in range(data_length)]
    open_cnt = [data[i]["prfprocnt"] for i in range(data_length)]
    run_cnt = [data[i]["prfdtcnt"] for i in range(data_length)]
    aud_shr = [data[i]["nmrsshr"] for i in range(data_length)]

    return genres, tickets, sales, sale_shr, open_cnt, run_cnt, aud_shr
