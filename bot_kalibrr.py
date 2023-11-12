import requests
import time
from termcolor import colored

# Header yang digunakan pada semua permintaan
headers = {
    'Content-Type': 'application/json',
    'Host': 'jobseeker.kalibrr.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'KB-CSRF': 'fOb0iNvQ7WD79c7Qyb89aluMh-Q~lZ3r',
    'Cookie': '_gcl_au=1.1.1800578442.1697982793; _ga_Q5JTLC9LMJ=GS1.1.1698219244.12.1.1698220054.23.0.0; _ga=GA1.1.623461414.1697982793; _ga_CYKC6J5VY2=GS1.1.1698219244.12.1.1698220054.0.0.0; _fbp=fb.1.1697982795644.608441384; _ga_X8GYQC04GE=GS1.1.1698219243.12.1.1698220050.0.0.0; _tac=true~kalibrr|not-available; _ta=id~4~c049fc44bc58fee86bfdf1181be24f43; __zlcmid=1ISmDQ8kMq7gGm5; session_ref=www.kalibrr.com_organic_null_path; kaid=%22d6fa4199-4598-4266-8020-01994a6f12db%22; kb="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYXhfYWdlIjoyNDE5MjAwLCJ1dGNfb2Zmc2V0Ijo0MjAsImxhc3RfbmFtZSI6Ikt1cm5pYXdhbiIsInRpbWVvdXQiOjEyMDk2MDAsInJvbGVzIjpbImNhbmRpZGF0ZSJdLCJ1c2VkX2dsb2JhbCI6ZmFsc2UsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJzdF9uYW1lIjoiRmlybWFuc3lhaCBIZWxtaSIsImlkIjo2MTY2ODYyLCJsb2NhbGUiOiJlbl9QSCIsImV4cGlyeV9kYXRlIjoiMjAyMy0xMC0yNSAwNzo1MjowMSIsImxvY2F0aW9uX2xvbmxhdCI6WzEwNi44NzI1MywtNi4yMzU1NV0sImNvdW50cnlfY29kZSI6IklEIiwidGltZSI6MTY5ODIyMDAyMS4zMjI1MzIsInNpZ251cF9icmFuZCI6ImthbGlicnIiLCJlbWFpbCI6Imt1cm5pYXdhbi5maXJtYW45NEBnbWFpbC5jb20iLCJtb2JpbGVfbnVtYmVyX2NvbmZpcm1lZCI6dHJ1ZSwibW9iaWxlX251bWJlcl9ub3JtYWxpemVkIjoiNjI4MTU4Njg0MzUyMiJ9.elReJeSgmNgzYfWaWmjqrHzIPZ46mJRWK8iCKKF3jSkMF9NCc5Nq9jIXfRza1TryEuCVOm-jX9xjGobVaLdHVcNl52_lxURmL_QMSwTv8J3YS-Y1owqb3fveQONRo5-91AbtudyTBWBzDF1BLiBKuIbEaREVgVlqKX114aJu-2aleclW-pIKo7GNbns48zkZDxXc2iuRjj2GHq1v_XkYoSmee74h1MxN7oSvkFdg11U3nlEJqtkHOue3sS_jmiZ-jsA899XkOEMUaQx8P74f_4PQdYtU7Dqt1hp6PKjFECR5JlvzxGkRZUJzqK_BHDhrr_AMLR1AO5GFDmL2NCM3_3yFcNxN3Iw51vmC73lNdNyD7h6hs1l4vuSqYa9WjYG6Dn3X1o8u3-h22I5Vf2UT2eFXZ3O5H4AmNV3NdZEW3Vbmrr4TXRYrcFf7kST4mHUjZ20EnV6gM77j2jHaDV_o4pUcO9z-tpi7rt9IQ5XWPUUJ0H1OAnxXLR5dw3WwcS1q94pwCI9RVbcvdWPgUNj4LFhIrWbnj8CH3kofOGsNfOYWhjVV24nqPRzd11GZqzIhzF5xIHCbmWGb8yknKA_hYnQd15FUmjG2wZhp4E9LZkaHb-GjyWmoTirfMe8J8uu1m1SXYbmVZWVVSnuh3rThPOEu0Nv1We8dVH32f_wSQz8"',
    # Isi dengan header request lainnya
}

# Fungsi untuk menampilkan daftar opsi dan meminta input dari pengguna
def get_user_input(options, title):
    while True:
        display_options(options, title)
        choice = input(f"Masukkan {title} (1-{len(options)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

# Fungsi untuk menampilkan daftar pilihan
def display_options(options, title):
    print(title + ":")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

# Fungsi untuk menampilkan pesan dengan warna
def color_message(message, color):
    print(colored(message, color))

def ambil_data_id(jenis_pekerjaan, job_level, employment_type, job_function, education_level, fast_response, limit):
    # Mapping pilihan pengguna ke nilai yang sesuai
    job_level_map = ["100,200,300,400,500", "100", "200", "300", "400", "500", ""]
    employment_type_map = ["Contractual,Freelance,Full%20time,Part%20time", "Full time", "Part time", "Freelance", "Contractual", ""]
    job_function_map = ["Accounting%20and%20Finance,Administration%20and%20Coordination,Architecture%20and%20Engineering,Arts%20and%20Sports,Customer%20Service,Education%20and%20Training,General%20Services,Health%20and%20Medical,Hospitality%20and%20Tourism,Human%20Resources,IT%20and%20Software,Legal,Management%20and%20Consultancy,Manufacturing%20and%20Production,Media%20and%20Creatives,Public%20Service%20and%20NGOs,Safety%20and%20Security,Sales%20and%20Marketing,Sciences,Skilled%20Trade,Supply%20Chain,Writing%20and%20Content", "Accounting and Finance", "Administration and Coordination", "Architecture and Engineering", "Arts and Sports", "Customer Service", "Education and Training", "General Services", "Health and Medical", "Hospitality and Tourism", "Human Resources", "IT and Software", "Legal", "Management and Consultancy", "Manufacturing and Production", "Media and Creatives", "Public Service and NGOs", "Safety and Security", "Sales and Marketing", "Sciences", "Skilled Trade", "Supply Chain", "Writing and Content", ""]
    education_level_map = ["100,150,200,300,350,400,450,500,550,600,650,700,750", "100", "150", "200", "300", "350", "400", "450", "500", "550", "600", "650", "700", "750"]
    fast_response_map = ["true", "false"]

    job_level_value = job_level_map[job_levels.index(job_level)]
    employment_type_value = employment_type_map[employment_types.index(employment_type)]
    job_function_value = job_function_map[job_functions.index(job_function)]
    education_level_value = education_level_map[education_levels.index(education_level)]
    fast_response_value = fast_response_map[fast_responses.index(fast_response)]

    url = f"https://jobseeker.kalibrr.com/kjs/job_board/search?limit={limit}&offset=0&text={jenis_pekerjaan}&work_experience={job_level_value}&tenure={employment_type_value}&function={job_function_value}&education_level={education_level_value}&responds_fast={fast_response_value}"
 
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        jobs = data.get('jobs', [])
        pendaftaran_berhasil = 0
        dilewati = 0
        jeda_counter = 0
        
        for job in jobs:
            job_id = job.get('id')
            company_name = job.get('company', {}).get('name', 'Nama Perusahaan Tidak Tersedia')
            job_title = job.get('name', 'Pekerjaan Tidak Tersedia')
            
            # Cek apakah pekerjaan sudah dilamar
            status_code = cek_lamaran(job_id)
            
            if status_code == 404:
                color_message(f"ID Pekerjaan: {job_id} - {company_name} - {job_title} - Sukses", 'green')
                pendaftaran = daftar_pekerjaan(job_id)
                if pendaftaran == 200:
                    pendaftaran_berhasil += 1
                else:
                    color_message(f"Pendaftaran gagal untuk ID Pekerjaan: {job_id}", 'red')
            elif status_code == 200:
                color_message(f"ID Pekerjaan: {job_id} - {company_name} - {job_title} - Terdaftar (Dilewati)", 'red')
                dilewati += 1
            else:
                color_message(f"ID Pekerjaan: {job_id} - {company_name} - {job_title} - Gagal memeriksa status lamaran", 'red')

            jeda_counter += 1
            if jeda_counter == 15:
                jeda_counter = 0
                # Jeda 10 detik setiap 15 perulangan
                time.sleep(10)
        
        color_message(f"Total Pendaftaran Berhasil: {pendaftaran_berhasil}", 'green')
        color_message(f"Total Dilewati: {dilewati}", 'red')
    else:
        color_message(f"Failed to fetch data. Status Code: {response.status_code}", 'red')

def cek_lamaran(job_id):
    url = f"https://jobseeker.kalibrr.com/api/candidate/job_applications/{job_id}"
    response = requests.get(url, headers=headers)
    return response.status_code

def daftar_pekerjaan(job_id):
    url = f"https://jobseeker.kalibrr.com/api/candidate/job_applications/{job_id}"
    payload = {"referrer": None, "session_referrer": "www.kalibrr.com_organic_null_path", "app_source": "job-full-page"}
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

# Daftar pilihan untuk setiap parameter
job_levels = ["All Job Levels", "Internship / OJT", "Entry Level / Junior", "Associate / Supervisor", "Mid-Senior Level / Manager", "Director / Executive", "Skip"]
employment_types = ["All Employment Types", "Full time", "Part time", "Freelance", "Contractual", "Skip"]
job_functions = ["All Job Functions", "Accounting and Finance", "Administration and Coordination", "Architecture and Engineering", "Arts and Sports", "Customer Service", "Education and Training", "General Services", "Health and Medical", "Hospitality and Tourism", "Human Resources", "IT and Software", "Legal", "Management and Consultancy", "Manufacturing and Production", "Media and Creatives", "Public Service and NGOs", "Safety and Security", "Sales and Marketing", "Sciences", "Skilled Trade", "Supply Chain", "Writing and Content", "Skip"]
education_levels = ["All Education Levels", "Less than high school", "High School", "Graduated from high school", "Vocational course", "Completed vocational course", "Associate's studies", "Completed associate's degree", "Bachelor's studies", "Bachelor's degree graduate", "Graduate studies (Masters)", "Master's degree graduate", "Post-graduate studies (Doctorate)", "Doctoral degree graduate"]
fast_responses = ["True", "False"]

# Meminta pengguna memilih nilai untuk setiap parameter
jenis_pekerjaan = input("Masukkan jenis pekerjaan: ")
job_level = get_user_input(job_levels, "Job Level")
employment_type = get_user_input(employment_types, "Employment Type")
job_function = get_user_input(job_functions, "Job Function")
education_level = get_user_input(education_levels, "Education Level")
fast_response = get_user_input(fast_responses, "Fast Response")
limit = input("Masukkan Limit: ")

ambil_data_id(jenis_pekerjaan, job_level, employment_type, job_function, education_level, fast_response, limit)