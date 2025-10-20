# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 02:37:52 2025

@author: numan
"""

def StudentTracking():
    print("Öğrenci Takip Uygulaması")
    idStudent = 1
    listStudent = []

    while True:
        choices = input("Öğrenci eklemek için (1), silmek için (2), listelemek için (3), çıkış için (0): ")

        if choices == "1":
            addName = input("Öğrenci ismi: ")
            addSurname = input("Öğrenci soyismi: ")
            addScore = float(input("Öğrenci notu: "))
            
            createStudent = {
                "id": idStudent,
                "Name": addName,
                "Surname": addSurname,
                "Score": addScore
            }
            listStudent.append(createStudent)
            idStudent += 1
            print(f"{addName} {addSurname} eklendi.")

        elif choices == "2":
            delStudent = int(input("Silmek istediğiniz öğrencinin ID'si: "))
            found = False
            for student in listStudent:
                if student["id"] == delStudent:
                    listStudent.remove(student)
                    print("Öğrenci silindi.")
                    found = True
                    break
            if not found:
                print("Öğrenci bulunamadı.")

        elif choices == "3":
            if len(listStudent) == 0:
                print("Liste boş.")
            else:
                for student in listStudent:
                    print(f"ID: {student['id']}, İsim: {student['Name']} {student['Surname']}, Not: {student['Score']:.2f}")

        elif choices == "0":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim!")
StudentTracking()
            
            
        