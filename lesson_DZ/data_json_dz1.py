__operator = ["istrati.a.a@gmail.com", "Анатолий"]
datas = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}

report_datas = {}

sum_one_two_delay = 0
total_count = 0
total_completed = 0
total_refunded = 0

for data in datas["data"]:
    assert ("_id" in data) is True
    if data["_id"] == "3d8c861f-e2c0-442a-9d82-810ae5eb5f52" or data["_id"] == "4816385b-a5a5-4341-aedf-6f80bedbdce4":
        sum_one_two_delay += data["delay"]
    assert sum_one_two_delay < 6  # уточнить 6 часов ключительно?
    if data["_id"] == "7e0882b5-38b8-4dcb-9825-625158a92314":
        assert data["delay"] // 2 < data["completed"]
        assert data["wait_refund"] < data["completed"]
        assert data["refunded"] > data["wait_refund"]
    report_datas.setdefault("list_id", []).append(data["_id"])
    total_count += data["count"]
    total_completed += data["completed"]
    total_refunded += data["refunded"]

report_datas["list_id"].append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")


def app_total_in_report(name, app: object):
    report_datas.setdefault("orders", {}).setdefault(f"{name}", app)


app_total_in_report("total_count", total_count)
app_total_in_report("total_completed", total_completed)
app_total_in_report("total_refunded", total_refunded)

print(__operator, report_datas, sep='\n')
