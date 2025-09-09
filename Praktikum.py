{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOzbzq3HfBzEfJv6eafxyH6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/siskamandasari/Siska-Mandasari_006_algoritma-pemograman/blob/main/Praktikum.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rXEAiG-d6GrJ",
        "outputId": "738cffd1-03a0-4d35-e20e-62992c8866df"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Kasus 1-Kendaraan darat\n",
            "Mobil A30.00 m/s\n",
            "Motor B10.00 m/s\n",
            "Sepeda C5.00 m/s\n",
            "Mobil_A tercepat\n",
            "\n",
            "Kasus 2 - Atlet Lari\n",
            "Pelari 1 = 8.00 m/s\n",
            "Pelari 2 = 6.67 m/s\n",
            "Pelari 3 = 9.09 m/s\n",
            "Pelari 3 tercepat\n",
            "\n",
            "Kasus 3 - Transportasi Umum\n",
            "Kereta = 27.78 m/s\n",
            "Bus = 25.00 m/s\n",
            "Truk = 20.83 m/s\n",
            "Kereta tercepat\n",
            "\n",
            "Kasus 4 - Udara, Laut, dan Darat\n",
            "Drone = 20.00 m/s\n",
            "Kapal Cepat = 16.67 m/s\n",
            "Pemain Sepak Bola = 8.57 m/s\n",
            "Drone tercepat\n"
          ]
        }
      ],
      "source": [
        "def hitung_kecepatan(jarak, waktu):\n",
        "    return jarak / waktu\n",
        "print(\"Kasus 1-Kendaraan darat\")\n",
        "mobil_A = hitung_kecepatan(1500, 50)\n",
        "motor_B = hitung_kecepatan(100, 10)\n",
        "sepeda_C = hitung_kecepatan(200, 40)\n",
        "print(f\"Mobil A{mobil_A:.2f} m/s\")\n",
        "print(f\"Motor B{motor_B:.2f} m/s\")\n",
        "print(f\"Sepeda C{sepeda_C:.2f} m/s\")\n",
        "if mobil_A > motor_B and mobil_A > sepeda_C:\n",
        "    print(\"Mobil_A tercepat\")\n",
        "elif motor_B > mobil_A and motor_B > sepeda_C:\n",
        "    print(\"Motor B tercepat\")\n",
        "else:\n",
        "    print(\"Sepeda C tercepat\")\n",
        "\n",
        "print()\n",
        "\n",
        "def hitung_kecepatan(jarak, waktu):\n",
        "    return jarak / waktu\n",
        "print(\"Kasus 2 - Atlet Lari\")\n",
        "pelari1 = hitung_kecepatan(400, 50)\n",
        "pelari2 = hitung_kecepatan(800, 120)\n",
        "pelari3 = hitung_kecepatan(100, 11)\n",
        "\n",
        "print(f\"Pelari 1 = {pelari1:.2f} m/s\")\n",
        "print(f\"Pelari 2 = {pelari2:.2f} m/s\")\n",
        "print(f\"Pelari 3 = {pelari3:.2f} m/s\")\n",
        "\n",
        "if pelari1 > pelari2 and pelari1 > pelari3:\n",
        "    print(\"Pelari 1 tercepat\")\n",
        "elif pelari2 > pelari1 and pelari2 > pelari3:\n",
        "    print(\"Pelari 2 tercepat\")\n",
        "else:\n",
        "    print(\"Pelari 3 tercepat\")\n",
        "\n",
        "print()\n",
        "\n",
        "def hitung_kecepatan(jarak, waktu):\n",
        "    return jarak / waktu\n",
        "print(\"Kasus 3 - Transportasi Umum\")\n",
        "kereta = hitung_kecepatan(5000, 180)\n",
        "bus = hitung_kecepatan(3000, 120)\n",
        "truk = hitung_kecepatan(2500, 120)\n",
        "\n",
        "print(f\"Kereta = {kereta:.2f} m/s\")\n",
        "print(f\"Bus = {bus:.2f} m/s\")\n",
        "print(f\"Truk = {truk:.2f} m/s\")\n",
        "\n",
        "if kereta > bus and kereta > truk:\n",
        "    print(\"Kereta tercepat\")\n",
        "elif bus > kereta and bus > truk:\n",
        "    print(\"Bus tercepat\")\n",
        "else:\n",
        "    print(\"Truk tercepat\")\n",
        "\n",
        "print()\n",
        "\n",
        "def hitung_kecepatan(jarak, waktu):\n",
        "    return jarak / waktu\n",
        "print(\"Kasus 4 - Udara, Laut, dan Darat\")\n",
        "drone = hitung_kecepatan(1200, 60)\n",
        "kapal = hitung_kecepatan(5000, 300)\n",
        "pemain = hitung_kecepatan(60, 7)\n",
        "\n",
        "print(f\"Drone = {drone:.2f} m/s\")\n",
        "print(f\"Kapal Cepat = {kapal:.2f} m/s\")\n",
        "print(f\"Pemain Sepak Bola = {pemain:.2f} m/s\")\n",
        "\n",
        "if drone > kapal and drone > pemain:\n",
        "    print(\"Drone tercepat\")\n",
        "elif kapal > drone and kapal > pemain:\n",
        "    print(\"Kapal tercepat\")\n",
        "else:\n",
        "    print(\"Pemain Sepak Bola tercepat\")"
      ]
    }
  ]
}