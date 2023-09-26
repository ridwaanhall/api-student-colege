import requests


def get_student_data(message_search):
    url = f"https://api-frontend.kemdikbud.go.id/hit_mhs/{message_search}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "Cari kata kunci" in data["mahasiswa"][0]["text"]:
            return []

        modified_data = {
            "mahasiswa": []
        }

        for student_info in data.get("mahasiswa", []):
            text = student_info.get("text", "")
            parts = text.split(", ")
            name_nim = parts[0].split("(")
            name = name_nim[0].strip()
            nim = name_nim[1].split(")")[0].strip()
            college_name = parts[1].split(": ")[1].strip()
            study_program = parts[2].split(": ")[1].strip()
            detail = student_info.get("website-link", "").split("/data_mahasiswa")[-1]

            modified_data["mahasiswa"].append({
                "student name": name,
                "nim": nim,
                "college name": college_name,
                "study program": study_program,
                "detail": detail
            })

        return modified_data

    return None


def get_student_detail(message_search):
    url = f"https://api-frontend.kemdikbud.go.id/detail_mhs/{message_search}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data

    return None