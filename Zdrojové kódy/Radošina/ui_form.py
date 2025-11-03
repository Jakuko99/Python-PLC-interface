# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTextBrowser,
    QWidget,
)


class Ui_ILTIS(object):
    def setupUi(self, ILTIS):
        if not ILTIS.objectName():
            ILTIS.setObjectName("ILTIS")
        ILTIS.setWindowModality(Qt.NonModal)
        ILTIS.resize(1920, 1080)
        ILTIS.setAutoFillBackground(False)
        ILTIS.setStyleSheet("background-color: rgb(0,0,0);")
        self.actionVo_ba_rozsahu_infoirm_ci = QAction(ILTIS)
        self.actionVo_ba_rozsahu_infoirm_ci.setObjectName(
            "actionVo_ba_rozsahu_infoirm_ci"
        )
        self.actionAlarm_vypn = QAction(ILTIS)
        self.actionAlarm_vypn.setObjectName("actionAlarm_vypn")
        self.actionHorizont_lne = QAction(ILTIS)
        self.actionHorizont_lne.setObjectName("actionHorizont_lne")
        self.actionVertik_lne = QAction(ILTIS)
        self.actionVertik_lne.setObjectName("actionVertik_lne")
        self.actionPozn_mka = QAction(ILTIS)
        self.actionPozn_mka.setObjectName("actionPozn_mka")
        self.actionPripomienka = QAction(ILTIS)
        self.actionPripomienka.setObjectName("actionPripomienka")
        self.actionZ_znam_makra_pr_kazov = QAction(ILTIS)
        self.actionZ_znam_makra_pr_kazov.setObjectName("actionZ_znam_makra_pr_kazov")
        self.actionObsluha_makra_pr_kazov = QAction(ILTIS)
        self.actionObsluha_makra_pr_kazov.setObjectName("actionObsluha_makra_pr_kazov")
        self.actionZobrazenie_protokolovania = QAction(ILTIS)
        self.actionZobrazenie_protokolovania.setObjectName(
            "actionZobrazenie_protokolovania"
        )
        self.actionProtokolovanie_Online = QAction(ILTIS)
        self.actionProtokolovanie_Online.setObjectName("actionProtokolovanie_Online")
        self.actionPr_kazy_tla_iarne = QAction(ILTIS)
        self.actionPr_kazy_tla_iarne.setObjectName("actionPr_kazy_tla_iarne")
        self.actionVo_ba_identifik_cie_funkcie = QAction(ILTIS)
        self.actionVo_ba_identifik_cie_funkcie.setObjectName(
            "actionVo_ba_identifik_cie_funkcie"
        )
        self.actionPrihl_senie = QAction(ILTIS)
        self.actionPrihl_senie.setObjectName("actionPrihl_senie")
        self.actionOdhl_senie = QAction(ILTIS)
        self.actionOdhl_senie.setObjectName("actionOdhl_senie")
        self.actionZavrie = QAction(ILTIS)
        self.actionZavrie.setObjectName("actionZavrie")
        self.actionVo_ba_profilu = QAction(ILTIS)
        self.actionVo_ba_profilu.setObjectName("actionVo_ba_profilu")
        self.actionNastacvenie_zvuku = QAction(ILTIS)
        self.actionNastacvenie_zvuku.setObjectName("actionNastacvenie_zvuku")
        self.actionZmena_hesla = QAction(ILTIS)
        self.actionZmena_hesla.setObjectName("actionZmena_hesla")
        self.actionVo_ba_tla_iarne = QAction(ILTIS)
        self.actionVo_ba_tla_iarne.setObjectName("actionVo_ba_tla_iarne")
        self.actionVo_ba_pracoviska_dr_by = QAction(ILTIS)
        self.actionVo_ba_pracoviska_dr_by.setObjectName("actionVo_ba_pracoviska_dr_by")
        self.actiondr_ba = QAction(ILTIS)
        self.actiondr_ba.setObjectName("actiondr_ba")
        self.actionTestovac_obraz_monitora = QAction(ILTIS)
        self.actionTestovac_obraz_monitora.setObjectName(
            "actionTestovac_obraz_monitora"
        )
        self.actionPreh_ad = QAction(ILTIS)
        self.actionPreh_ad.setObjectName("actionPreh_ad")
        self.actionRozsah_inform_ci = QAction(ILTIS)
        self.actionRozsah_inform_ci.setObjectName("actionRozsah_inform_ci")
        self.actionProfil = QAction(ILTIS)
        self.actionProfil.setObjectName("actionProfil")
        self.actionPracovisk = QAction(ILTIS)
        self.actionPracovisk.setObjectName("actionPracovisk")
        self.actionIdentifik_cie_funkcie = QAction(ILTIS)
        self.actionIdentifik_cie_funkcie.setObjectName("actionIdentifik_cie_funkcie")
        self.actionIdentifik_cie_u_vate_a = QAction(ILTIS)
        self.actionIdentifik_cie_u_vate_a.setObjectName("actionIdentifik_cie_u_vate_a")
        self.actionInfo = QAction(ILTIS)
        self.actionInfo.setObjectName("actionInfo")
        self.actionKontext = QAction(ILTIS)
        self.actionKontext.setObjectName("actionKontext")
        self.actionVlastnosti = QAction(ILTIS)
        self.actionVlastnosti.setObjectName("actionVlastnosti")
        self.centralwidget = QWidget(ILTIS)
        self.centralwidget.setObjectName("centralwidget")
        self.RAD_k1 = QPushButton(self.centralwidget)
        self.RAD_k1.setObjectName("RAD_k1")
        self.RAD_k1.setGeometry(QRect(470, 292, 125, 59))
        icon = QIcon()
        icon.addFile("img/Kolaj/Kol_st1_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_k1.setIcon(icon)
        self.RAD_k1.setIconSize(QSize(125, 59))
        self.RAD_k1.setAutoDefault(False)
        self.RAD_k1.setFlat(False)
        self.RAD_k2 = QPushButton(self.centralwidget)
        self.RAD_k2.setObjectName("RAD_k2")
        self.RAD_k2.setGeometry(QRect(470, 350, 125, 59))
        icon1 = QIcon()
        icon1.addFile("img/Kolaj/Kol_st2_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_k2.setIcon(icon1)
        self.RAD_k2.setIconSize(QSize(125, 59))
        self.RAD_k2.setAutoDefault(False)
        self.RAD_k2.setFlat(False)
        self.RAD_L1 = QPushButton(self.centralwidget)
        self.RAD_L1.setObjectName("RAD_L1")
        self.RAD_L1.setGeometry(QRect(595, 293, 52, 58))
        icon2 = QIcon()
        icon2.addFile(
            "img/HlavneKombinovaneNav/Kom_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.RAD_L1.setIcon(icon2)
        self.RAD_L1.setIconSize(QSize(68, 59))
        self.RAD_L1.setAutoDefault(False)
        self.RAD_L1.setFlat(False)
        self.RAD_L2 = QPushButton(self.centralwidget)
        self.RAD_L2.setObjectName("RAD_L2")
        self.RAD_L2.setGeometry(QRect(595, 351, 52, 58))
        self.RAD_L2.setIcon(icon2)
        self.RAD_L2.setIconSize(QSize(68, 59))
        self.RAD_L2.setAutoDefault(False)
        self.RAD_L2.setFlat(False)
        self.RAD_V1 = QPushButton(self.centralwidget)
        self.RAD_V1.setObjectName("RAD_V1")
        self.RAD_V1.setGeometry(QRect(647, 288, 117, 125))
        icon3 = QIcon()
        icon3.addFile("img/Vyhybka/VyhPH_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_V1.setIcon(icon3)
        self.RAD_V1.setIconSize(QSize(125, 118))
        self.RAD_V1.setAutoDefault(False)
        self.RAD_V1.setFlat(False)
        self.RAD_fik_S = QPushButton(self.centralwidget)
        self.RAD_fik_S.setObjectName("RAD_fik_S")
        self.RAD_fik_S.setGeometry(QRect(934, 300, 23, 43))
        icon4 = QIcon()
        icon4.addFile("img/Fiktivne/Fikt_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_fik_S.setIcon(icon4)
        self.RAD_fik_S.setIconSize(QSize(23, 43))
        self.RAD_fik_S.setAutoDefault(False)
        self.RAD_fik_S.setFlat(False)
        self.RAD_zr_do_st_odZ = QPushButton(self.centralwidget)
        self.RAD_zr_do_st_odZ.setObjectName("RAD_zr_do_st_odZ")
        self.RAD_zr_do_st_odZ.setGeometry(QRect(763, 300, 23, 43))
        icon5 = QIcon()
        icon5.addFile("img/Zriad/Zriad_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_zr_do_st_odZ.setIcon(icon5)
        self.RAD_zr_do_st_odZ.setIconSize(QSize(68, 59))
        self.RAD_zr_do_st_odZ.setAutoDefault(False)
        self.RAD_zr_do_st_odZ.setFlat(False)
        self.RAD_Sk = QPushButton(self.centralwidget)
        self.RAD_Sk.setObjectName("RAD_Sk")
        self.RAD_Sk.setGeometry(QRect(786, 291, 125, 59))
        icon6 = QIcon()
        icon6.addFile("img/Kolaj/Kol_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_Sk.setIcon(icon6)
        self.RAD_Sk.setIconSize(QSize(125, 59))
        self.RAD_Sk.setAutoDefault(False)
        self.RAD_Sk.setFlat(False)
        self.RAD_zr_zo_st_odZ = QPushButton(self.centralwidget)
        self.RAD_zr_zo_st_odZ.setObjectName("RAD_zr_zo_st_odZ")
        self.RAD_zr_zo_st_odZ.setGeometry(QRect(911, 300, 23, 43))
        icon7 = QIcon()
        icon7.addFile("img/Zriad/Zriad_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_zr_zo_st_odZ.setIcon(icon7)
        self.RAD_zr_zo_st_odZ.setIconSize(QSize(68, 59))
        self.RAD_zr_zo_st_odZ.setAutoDefault(False)
        self.RAD_zr_zo_st_odZ.setFlat(False)
        self.RAD_ZBE_TU1 = QPushButton(self.centralwidget)
        self.RAD_ZBE_TU1.setObjectName("RAD_ZBE_TU1")
        self.RAD_ZBE_TU1.setGeometry(QRect(995, 291, 125, 59))
        self.RAD_ZBE_TU1.setIcon(icon6)
        self.RAD_ZBE_TU1.setIconSize(QSize(125, 59))
        self.RAD_ZBE_TU1.setAutoDefault(False)
        self.RAD_ZBE_TU1.setFlat(False)
        self.RAD_S = QPushButton(self.centralwidget)
        self.RAD_S.setObjectName("RAD_S")
        self.RAD_S.setGeometry(QRect(957, 293, 38, 58))
        icon8 = QIcon()
        icon8.addFile("img/HlavneNav/Hl_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_S.setIcon(icon8)
        self.RAD_S.setIconSize(QSize(38, 58))
        self.RAD_S.setAutoDefault(False)
        self.RAD_S.setFlat(False)
        self.RAD_trat_suhlas_doZ = QPushButton(self.centralwidget)
        self.RAD_trat_suhlas_doZ.setObjectName("RAD_trat_suhlas_doZ")
        self.RAD_trat_suhlas_doZ.setGeometry(QRect(1002, 347, 39, 18))
        icon9 = QIcon()
        icon9.addFile("img/TS/TS_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_trat_suhlas_doZ.setIcon(icon9)
        self.RAD_trat_suhlas_doZ.setIconSize(QSize(39, 18))
        self.RAD_trat_suhlas_doZ.setAutoDefault(False)
        self.RAD_trat_suhlas_doZ.setFlat(False)
        self.RAD_dialkove = QPushButton(self.centralwidget)
        self.RAD_dialkove.setObjectName("RAD_dialkove")
        self.RAD_dialkove.setGeometry(QRect(538, 233, 58, 43))
        icon10 = QIcon()
        icon10.addFile("img/Stanice/RAD_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_dialkove.setIcon(icon10)
        self.RAD_dialkove.setIconSize(QSize(58, 43))
        self.RAD_ASVC = QPushButton(self.centralwidget)
        self.RAD_ASVC.setObjectName("RAD_ASVC")
        self.RAD_ASVC.setGeometry(QRect(598, 233, 58, 43))
        icon11 = QIcon()
        icon11.addFile("img/Stanice/ASVC_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_ASVC.setIcon(icon11)
        self.RAD_ASVC.setIconSize(QSize(58, 43))
        self.RAD_fik_29 = QPushButton(self.centralwidget)
        self.RAD_fik_29.setObjectName("RAD_fik_29")
        self.RAD_fik_29.setGeometry(QRect(1320, 299, 23, 43))
        self.RAD_fik_29.setIcon(icon4)
        self.RAD_fik_29.setIconSize(QSize(23, 43))
        self.RAD_fik_29.setAutoDefault(False)
        self.RAD_fik_29.setFlat(False)
        self.textZbehy = QLabel(self.centralwidget)
        self.textZbehy.setObjectName("textZbehy")
        self.textZbehy.setGeometry(QRect(1340, 250, 81, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.textZbehy.setFont(font)
        self.textZbehy.setTextFormat(Qt.AutoText)
        self.textZbehy.setScaledContents(True)
        self.RAD_pracovisko = QLabel(self.centralwidget)
        self.RAD_pracovisko.setObjectName("RAD_pracovisko")
        self.RAD_pracovisko.setGeometry(QRect(468, 233, 55, 38))
        self.RAD_pracovisko.setFont(font)
        self.RAD_pracovisko.setTextFormat(Qt.AutoText)
        self.RAD_pracovisko.setPixmap(QPixmap("img/Stanice/Pracovisko.bmp"))
        self.RAD_pracovisko.setScaledContents(True)
        self.combo_hlavne = QComboBox(self.centralwidget)
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.setObjectName("combo_hlavne")
        self.combo_hlavne.setGeometry(QRect(660, 470, 72, 24))
        self.combo_hlavne.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_zriad = QComboBox(self.centralwidget)
        self.combo_zriad.addItem("")
        self.combo_zriad.addItem("")
        self.combo_zriad.addItem("")
        self.combo_zriad.addItem("")
        self.combo_zriad.addItem("")
        self.combo_zriad.setObjectName("combo_zriad")
        self.combo_zriad.setGeometry(QRect(660, 470, 72, 24))
        self.combo_zriad.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_vyh = QComboBox(self.centralwidget)
        self.combo_vyh.addItem("")
        self.combo_vyh.addItem("")
        self.combo_vyh.addItem("")
        self.combo_vyh.setObjectName("combo_vyh")
        self.combo_vyh.setGeometry(QRect(690, 420, 72, 24))
        self.combo_vyh.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_kombi = QComboBox(self.centralwidget)
        self.combo_kombi.addItem("")
        self.combo_kombi.addItem("")
        self.combo_kombi.addItem("")
        self.combo_kombi.addItem("")
        self.combo_kombi.addItem("")
        self.combo_kombi.addItem("")
        self.combo_kombi.addItem("")
        self.combo_kombi.setObjectName("combo_kombi")
        self.combo_kombi.setGeometry(QRect(660, 470, 72, 24))
        self.combo_kombi.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.RAD_1k_fik = QPushButton(self.centralwidget)
        self.RAD_1k_fik.setObjectName("RAD_1k_fik")
        self.RAD_1k_fik.setGeometry(QRect(418, 293, 52, 58))
        icon12 = QIcon()
        icon12.addFile(
            "img/HlavneKombinovaneNav/Kom_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.RAD_1k_fik.setIcon(icon12)
        self.RAD_1k_fik.setIconSize(QSize(68, 59))
        self.RAD_1k_fik.setAutoDefault(False)
        self.RAD_1k_fik.setFlat(False)
        self.RAD_2k_fik = QPushButton(self.centralwidget)
        self.RAD_2k_fik.setObjectName("RAD_2k_fik")
        self.RAD_2k_fik.setGeometry(QRect(418, 351, 52, 58))
        self.RAD_2k_fik.setIcon(icon12)
        self.RAD_2k_fik.setIconSize(QSize(68, 59))
        self.RAD_2k_fik.setAutoDefault(False)
        self.RAD_2k_fik.setFlat(False)
        self.textRadosina = QLabel(self.centralwidget)
        self.textRadosina.setObjectName("textRadosina")
        self.textRadosina.setGeometry(QRect(540, 180, 111, 51))
        self.RAD_k2_kon = QLabel(self.centralwidget)
        self.RAD_k2_kon.setObjectName("RAD_k2_kon")
        self.RAD_k2_kon.setGeometry(QRect(415, 350, 3, 60))
        self.RAD_k2_kon.setPixmap(QPixmap("img/Kolaj/Kol_koniec_volna.bmp"))
        self.RAD_k1_kon = QLabel(self.centralwidget)
        self.RAD_k1_kon.setObjectName("RAD_k1_kon")
        self.RAD_k1_kon.setGeometry(QRect(415, 292, 3, 60))
        self.RAD_k1_kon.setPixmap(QPixmap("img/Kolaj/Kol_koniec_volna.bmp"))
        self.combo_fikt = QComboBox(self.centralwidget)
        self.combo_fikt.addItem("")
        self.combo_fikt.addItem("")
        self.combo_fikt.setObjectName("combo_fikt")
        self.combo_fikt.setGeometry(QRect(660, 470, 72, 24))
        self.combo_fikt.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_ciel_ko = QComboBox(self.centralwidget)
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.setObjectName("combo_ciel_ko")
        self.combo_ciel_ko.setGeometry(QRect(660, 495, 72, 24))
        self.combo_ciel_ko.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_ciel_zr = QComboBox(self.centralwidget)
        self.combo_ciel_zr.addItem("")
        self.combo_ciel_zr.addItem("")
        self.combo_ciel_zr.setObjectName("combo_ciel_zr")
        self.combo_ciel_zr.setGeometry(QRect(660, 495, 72, 24))
        self.combo_ciel_zr.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_ciel_fi = QComboBox(self.centralwidget)
        self.combo_ciel_fi.addItem("")
        self.combo_ciel_fi.addItem("")
        self.combo_ciel_fi.setObjectName("combo_ciel_fi")
        self.combo_ciel_fi.setGeometry(QRect(660, 495, 72, 24))
        self.combo_ciel_fi.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.RAD_ZBE_TU2_1 = QPushButton(self.centralwidget)
        self.RAD_ZBE_TU2_1.setObjectName("RAD_ZBE_TU2_1")
        self.RAD_ZBE_TU2_1.setGeometry(QRect(1196, 290, 51, 59))
        self.RAD_ZBE_TU2_1.setIcon(icon6)
        self.RAD_ZBE_TU2_1.setIconSize(QSize(125, 59))
        self.RAD_ZBE_TU2_1.setAutoDefault(False)
        self.RAD_ZBE_TU2_1.setFlat(False)
        self.RAD_ZBE_priec = QPushButton(self.centralwidget)
        self.RAD_ZBE_priec.setObjectName("RAD_ZBE_priec")
        self.RAD_ZBE_priec.setGeometry(QRect(1247, 295, 22, 53))
        icon13 = QIcon()
        icon13.addFile(
            "img/Priecestie/Priec_basic.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.RAD_ZBE_priec.setIcon(icon13)
        self.RAD_ZBE_priec.setIconSize(QSize(22, 53))
        self.RAD_ZBE_priec.setAutoDefault(False)
        self.RAD_ZBE_priec.setFlat(False)
        self.RAD_ZBE_TU2_2 = QPushButton(self.centralwidget)
        self.RAD_ZBE_TU2_2.setObjectName("RAD_ZBE_TU2_2")
        self.RAD_ZBE_TU2_2.setGeometry(QRect(1269, 290, 51, 59))
        self.RAD_ZBE_TU2_2.setIcon(icon6)
        self.RAD_ZBE_TU2_2.setIconSize(QSize(125, 59))
        self.RAD_ZBE_TU2_2.setAutoDefault(False)
        self.RAD_ZBE_TU2_2.setFlat(False)
        self.combo_TS_ZBE = QComboBox(self.centralwidget)
        self.combo_TS_ZBE.addItem("")
        self.combo_TS_ZBE.addItem("")
        self.combo_TS_ZBE.addItem("")
        self.combo_TS_ZBE.addItem("")
        self.combo_TS_ZBE.setObjectName("combo_TS_ZBE")
        self.combo_TS_ZBE.setGeometry(QRect(980, 380, 72, 24))
        self.combo_TS_ZBE.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_priec = QComboBox(self.centralwidget)
        self.combo_priec.addItem("")
        self.combo_priec.addItem("")
        self.combo_priec.addItem("")
        self.combo_priec.setObjectName("combo_priec")
        self.combo_priec.setGeometry(QRect(1220, 370, 72, 24))
        self.combo_priec.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.RAD_ZBE_18 = QPushButton(self.centralwidget)
        self.RAD_ZBE_18.setObjectName("RAD_ZBE_18")
        self.RAD_ZBE_18.setGeometry(QRect(1158, 292, 38, 58))
        self.RAD_ZBE_18.setIcon(icon8)
        self.RAD_ZBE_18.setIconSize(QSize(38, 58))
        self.RAD_ZBE_18.setAutoDefault(False)
        self.RAD_ZBE_18.setFlat(False)
        self.RAD_ZBE_19 = QPushButton(self.centralwidget)
        self.RAD_ZBE_19.setObjectName("RAD_ZBE_19")
        self.RAD_ZBE_19.setGeometry(QRect(1120, 293, 38, 58))
        icon14 = QIcon()
        icon14.addFile("img/HlavneNav/Hl_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_ZBE_19.setIcon(icon14)
        self.RAD_ZBE_19.setIconSize(QSize(38, 58))
        self.RAD_ZBE_19.setAutoDefault(False)
        self.RAD_ZBE_19.setFlat(False)
        self.combo_Riadenie = QComboBox(self.centralwidget)
        self.combo_Riadenie.addItem("")
        self.combo_Riadenie.addItem("")
        self.combo_Riadenie.addItem("")
        self.combo_Riadenie.setObjectName("combo_Riadenie")
        self.combo_Riadenie.setGeometry(QRect(733, 470, 72, 24))
        self.combo_Riadenie.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.groupREST = QGroupBox(self.centralwidget)
        self.groupREST.setObjectName("groupREST")
        self.groupREST.setGeometry(QRect(900, 269, 166, 140))
        self.groupREST.setStyleSheet(
            "background-color: rgb(166, 166, 166);\n" "color: rgb(0, 0, 0);"
        )
        self.ButtonClose = QPushButton(self.groupREST)
        self.ButtonClose.setObjectName("ButtonClose")
        self.ButtonClose.setGeometry(QRect(146, 0, 20, 20))
        font1 = QFont()
        font1.setBold(True)
        self.ButtonClose.setFont(font1)
        self.ButtonClose.setAutoFillBackground(False)
        self.ButtonClose.setStyleSheet(
            "background-color: rgb(255, 0, 0);\n" "color: rgb(0, 0, 0);"
        )
        self.Line_IP = QLineEdit(self.groupREST)
        self.Line_IP.setObjectName("Line_IP")
        self.Line_IP.setGeometry(QRect(27, 50, 115, 24))
        self.Line_IP.setStyleSheet(
            "background-color: rgb(190, 190, 190);\n" "color: rgb(0, 0, 0);"
        )
        self.ButtonConnect = QPushButton(self.groupREST)
        self.ButtonConnect.setObjectName("ButtonConnect")
        self.ButtonConnect.setGeometry(QRect(47, 80, 80, 24))
        self.ButtonConnect.setFont(font1)
        self.ButtonConnect.setAutoFillBackground(False)
        self.ButtonConnect.setStyleSheet(
            "background-color: rgb(25, 170, 0);\n" "color: rgb(0, 0, 0);"
        )
        self.ButtonDisconnect = QPushButton(self.groupREST)
        self.ButtonDisconnect.setObjectName("ButtonDisconnect")
        self.ButtonDisconnect.setGeometry(QRect(47, 110, 80, 24))
        self.ButtonDisconnect.setFont(font1)
        self.ButtonDisconnect.setAutoFillBackground(False)
        self.ButtonDisconnect.setStyleSheet(
            "background-color: rgb(255, 0, 0);\n" "color: rgb(0, 0, 0);"
        )
        self.textConnection = QLabel(self.groupREST)
        self.textConnection.setObjectName("textConnection")
        self.textConnection.setGeometry(QRect(30, 30, 131, 21))
        self.textConnection.setFont(font)
        self.textConnection.setStyleSheet("color: rgb(0,0,0);")
        self.textConnection.setTextFormat(Qt.AutoText)
        self.textConnection.setScaledContents(True)
        self.groupCentrala = QGroupBox(self.centralwidget)
        self.groupCentrala.setObjectName("groupCentrala")
        self.groupCentrala.setGeometry(QRect(0, 830, 1920, 201))
        self.groupCentrala.setStyleSheet(
            "background-color: rgb(166, 166, 166);\n"
            'font: 9pt "Segoe UI";\n'
            "color: rgb(0, 0, 0);\n"
            'font: 700 18pt "Segoe UI";'
        )
        self.groupSystem = QGroupBox(self.groupCentrala)
        self.groupSystem.setObjectName("groupSystem")
        self.groupSystem.setGeometry(QRect(1440, 36, 478, 163))
        self.groupSystem.setStyleSheet(
            "color: rgb(166, 166, 166);\n"
            'font: 700 12pt "Segoe UI";\n'
            "background-color: rgb(0, 0, 0);"
        )
        self.groupPoruchy = QGroupBox(self.groupCentrala)
        self.groupPoruchy.setObjectName("groupPoruchy")
        self.groupPoruchy.setGeometry(QRect(960, 36, 478, 163))
        self.groupPoruchy.setStyleSheet(
            'font: 700 12pt "Segoe UI";\n'
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(166, 166, 166);"
        )
        self.textChybaREST = QLabel(self.groupPoruchy)
        self.textChybaREST.setObjectName("textChybaREST")
        self.textChybaREST.setGeometry(QRect(15, 30, 261, 21))
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.textChybaREST.setFont(font2)
        self.textChybaREST.setStyleSheet("color: rgb(166, 166, 166);")
        self.textChybaREST.setTextFormat(Qt.AutoText)
        self.textChybaREST.setScaledContents(True)
        self.groupHlasenia = QGroupBox(self.groupCentrala)
        self.groupHlasenia.setObjectName("groupHlasenia")
        self.groupHlasenia.setGeometry(QRect(480, 36, 478, 163))
        self.groupHlasenia.setStyleSheet(
            'font: 700 12pt "Segoe UI";\n'
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(166, 166, 166);"
        )
        self.textHlasenia = QTextBrowser(self.groupHlasenia)
        self.textHlasenia.setObjectName("textHlasenia")
        self.textHlasenia.setGeometry(QRect(0, 24, 478, 139))
        self.groupHlasenia_2 = QGroupBox(self.groupCentrala)
        self.groupHlasenia_2.setObjectName("groupHlasenia_2")
        self.groupHlasenia_2.setGeometry(QRect(1, 36, 476, 163))
        self.groupHlasenia_2.setStyleSheet(
            'font: 700 12pt "Segoe UI";\n'
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(166, 166, 166);"
        )
        self.DateTime = QLabel(self.centralwidget)
        self.DateTime.setObjectName("DateTime")
        self.DateTime.setGeometry(QRect(1769, 0, 151, 21))
        self.DateTime.setStyleSheet(
            "background-color: rgb(166, 166, 166);\n"
            'font: 700 12pt "Segoe UI";\n'
            "color: rgb(0, 0, 0);"
        )
        self.groupPrehlad = QGroupBox(self.centralwidget)
        self.groupPrehlad.setObjectName("groupPrehlad")
        self.groupPrehlad.setGeometry(QRect(919, 269, 128, 135))
        self.groupPrehlad.setStyleSheet(
            "background-color: rgb(166, 166, 166);\n" "color: rgb(0, 0, 0);"
        )
        self.label_4 = QLabel(self.groupPrehlad)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(0, 34, 125, 16))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.ButtonClose_1 = QPushButton(self.groupPrehlad)
        self.ButtonClose_1.setObjectName("ButtonClose_1")
        self.ButtonClose_1.setGeometry(QRect(108, 0, 20, 20))
        self.ButtonClose_1.setFont(font1)
        self.ButtonClose_1.setAutoFillBackground(False)
        self.ButtonClose_1.setStyleSheet(
            "background-color: rgb(255, 0, 0);\n" "color: rgb(0, 0, 0);"
        )
        self.label_5 = QLabel(self.groupPrehlad)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(0, 75, 125, 16))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.groupPrehlad)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(0, 50, 125, 16))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupPrehlad)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(0, 100, 125, 16))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.groupPrehlad)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(0, 115, 125, 16))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.groupPrehlad)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(0, 20, 125, 16))
        self.label_9.setAlignment(Qt.AlignCenter)
        ILTIS.setCentralWidget(self.centralwidget)
        self.RAD_k2.raise_()
        self.RAD_L1.raise_()
        self.RAD_L2.raise_()
        self.RAD_V1.raise_()
        self.RAD_k1.raise_()
        self.RAD_fik_S.raise_()
        self.RAD_zr_do_st_odZ.raise_()
        self.RAD_Sk.raise_()
        self.RAD_zr_zo_st_odZ.raise_()
        self.RAD_ZBE_TU1.raise_()
        self.RAD_S.raise_()
        self.RAD_trat_suhlas_doZ.raise_()
        self.RAD_dialkove.raise_()
        self.RAD_ASVC.raise_()
        self.RAD_fik_29.raise_()
        self.textZbehy.raise_()
        self.RAD_pracovisko.raise_()
        self.combo_hlavne.raise_()
        self.combo_zriad.raise_()
        self.combo_vyh.raise_()
        self.combo_kombi.raise_()
        self.RAD_1k_fik.raise_()
        self.RAD_2k_fik.raise_()
        self.textRadosina.raise_()
        self.RAD_k2_kon.raise_()
        self.RAD_k1_kon.raise_()
        self.combo_fikt.raise_()
        self.combo_ciel_ko.raise_()
        self.combo_ciel_zr.raise_()
        self.combo_ciel_fi.raise_()
        self.RAD_ZBE_TU2_1.raise_()
        self.RAD_ZBE_priec.raise_()
        self.RAD_ZBE_TU2_2.raise_()
        self.combo_TS_ZBE.raise_()
        self.combo_priec.raise_()
        self.RAD_ZBE_18.raise_()
        self.RAD_ZBE_19.raise_()
        self.combo_Riadenie.raise_()
        self.groupREST.raise_()
        self.groupCentrala.raise_()
        self.DateTime.raise_()
        self.groupPrehlad.raise_()
        self.menubar = QMenuBar(ILTIS)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 21))
        self.menubar.setStyleSheet(
            "background-color: rgb(166, 166, 166);\n" "color: rgb(0, 0, 0);"
        )
        self.menuSyst_m = QMenu(self.menubar)
        self.menuSyst_m.setObjectName("menuSyst_m")
        self.menuSpr_va_hl_sen = QMenu(self.menuSyst_m)
        self.menuSpr_va_hl_sen.setObjectName("menuSpr_va_hl_sen")
        self.menu_V_RD = QMenu(self.menubar)
        self.menu_V_RD.setObjectName("menu_V_RD")
        self.menuKonfigur_cia = QMenu(self.menubar)
        self.menuKonfigur_cia.setObjectName("menuKonfigur_cia")
        self.menuSpr_va_syst_mu = QMenu(self.menuKonfigur_cia)
        self.menuSpr_va_syst_mu.setObjectName("menuSpr_va_syst_mu")
        self.menuPomoc = QMenu(self.menubar)
        self.menuPomoc.setObjectName("menuPomoc")
        self.menuREST_server = QMenu(self.menubar)
        self.menuREST_server.setObjectName("menuREST_server")
        ILTIS.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ILTIS)
        self.statusbar.setObjectName("statusbar")
        ILTIS.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSyst_m.menuAction())
        self.menubar.addAction(self.menu_V_RD.menuAction())
        self.menubar.addAction(self.menuKonfigur_cia.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())
        self.menubar.addAction(self.menuREST_server.menuAction())
        self.menuSyst_m.addAction(self.actionVo_ba_rozsahu_infoirm_ci)
        self.menuSyst_m.addSeparator()
        self.menuSyst_m.addAction(self.actionAlarm_vypn)
        self.menuSyst_m.addAction(self.menuSpr_va_hl_sen.menuAction())
        self.menuSyst_m.addSeparator()
        self.menuSyst_m.addAction(self.actionPozn_mka)
        self.menuSyst_m.addAction(self.actionPripomienka)
        self.menuSyst_m.addSeparator()
        self.menuSyst_m.addAction(self.actionZ_znam_makra_pr_kazov)
        self.menuSyst_m.addAction(self.actionObsluha_makra_pr_kazov)
        self.menuSyst_m.addSeparator()
        self.menuSyst_m.addAction(self.actionZobrazenie_protokolovania)
        self.menuSyst_m.addAction(self.actionProtokolovanie_Online)
        self.menuSyst_m.addSeparator()
        self.menuSyst_m.addAction(self.actionPr_kazy_tla_iarne)
        self.menuSyst_m.addSeparator()
        self.menuSyst_m.addAction(self.actionVo_ba_identifik_cie_funkcie)
        self.menuSyst_m.addAction(self.actionPrihl_senie)
        self.menuSyst_m.addAction(self.actionOdhl_senie)
        self.menuSyst_m.addAction(self.actionZavrie)
        self.menuSpr_va_hl_sen.addAction(self.actionHorizont_lne)
        self.menuSpr_va_hl_sen.addAction(self.actionVertik_lne)
        self.menuKonfigur_cia.addAction(self.actionVo_ba_profilu)
        self.menuKonfigur_cia.addAction(self.actionNastacvenie_zvuku)
        self.menuKonfigur_cia.addAction(self.actionZmena_hesla)
        self.menuKonfigur_cia.addAction(self.actionVo_ba_tla_iarne)
        self.menuKonfigur_cia.addSeparator()
        self.menuKonfigur_cia.addAction(self.menuSpr_va_syst_mu.menuAction())
        self.menuKonfigur_cia.addSeparator()
        self.menuKonfigur_cia.addAction(self.actionVo_ba_pracoviska_dr_by)
        self.menuKonfigur_cia.addAction(self.actiondr_ba)
        self.menuKonfigur_cia.addAction(self.actionTestovac_obraz_monitora)
        self.menuKonfigur_cia.addSeparator()
        self.menuKonfigur_cia.addAction(self.actionPreh_ad)
        self.menuSpr_va_syst_mu.addAction(self.actionRozsah_inform_ci)
        self.menuSpr_va_syst_mu.addAction(self.actionProfil)
        self.menuSpr_va_syst_mu.addAction(self.actionPracovisk)
        self.menuSpr_va_syst_mu.addAction(self.actionIdentifik_cie_funkcie)
        self.menuSpr_va_syst_mu.addAction(self.actionIdentifik_cie_u_vate_a)
        self.menuPomoc.addAction(self.actionInfo)
        self.menuPomoc.addAction(self.actionKontext)
        self.menuREST_server.addAction(self.actionVlastnosti)

        self.retranslateUi(ILTIS)

        self.RAD_k1.setDefault(False)
        self.RAD_k2.setDefault(False)
        self.RAD_L1.setDefault(False)
        self.RAD_L2.setDefault(False)
        self.RAD_V1.setDefault(False)
        self.RAD_fik_S.setDefault(False)
        self.RAD_zr_do_st_odZ.setDefault(False)
        self.RAD_Sk.setDefault(False)
        self.RAD_zr_zo_st_odZ.setDefault(False)
        self.RAD_ZBE_TU1.setDefault(False)
        self.RAD_S.setDefault(False)
        self.RAD_trat_suhlas_doZ.setDefault(False)
        self.RAD_fik_29.setDefault(False)
        self.RAD_1k_fik.setDefault(False)
        self.RAD_2k_fik.setDefault(False)
        self.RAD_ZBE_TU2_1.setDefault(False)
        self.RAD_ZBE_priec.setDefault(False)
        self.RAD_ZBE_TU2_2.setDefault(False)
        self.RAD_ZBE_18.setDefault(False)
        self.RAD_ZBE_19.setDefault(False)

        QMetaObject.connectSlotsByName(ILTIS)

    # setupUi

    def retranslateUi(self, ILTIS):
        ILTIS.setWindowTitle(QCoreApplication.translate("ILTIS", "App", None))
        self.actionVo_ba_rozsahu_infoirm_ci.setText(
            QCoreApplication.translate(
                "ILTIS", "Vo\u013eba rozsahu infoirm\u00e1ci\u00ed", None
            )
        )
        self.actionAlarm_vypn.setText(
            QCoreApplication.translate("ILTIS", "Alarm vypn\u00fa\u0165", None)
        )
        self.actionHorizont_lne.setText(
            QCoreApplication.translate("ILTIS", "Horizont\u00e1lne", None)
        )
        self.actionVertik_lne.setText(
            QCoreApplication.translate("ILTIS", "Vertik\u00e1lne", None)
        )
        self.actionPozn_mka.setText(
            QCoreApplication.translate("ILTIS", "Pozn\u00e1mka ...", None)
        )
        self.actionPripomienka.setText(
            QCoreApplication.translate("ILTIS", "Pripomienka ...", None)
        )
        self.actionZ_znam_makra_pr_kazov.setText(
            QCoreApplication.translate(
                "ILTIS", "Z\u00e1znam makra pr\u00edkazov ...", None
            )
        )
        self.actionObsluha_makra_pr_kazov.setText(
            QCoreApplication.translate("ILTIS", "Obsluha makra pr\u00edkazov ...", None)
        )
        self.actionZobrazenie_protokolovania.setText(
            QCoreApplication.translate("ILTIS", "Zobrazenie protokolovania ...", None)
        )
        self.actionProtokolovanie_Online.setText(
            QCoreApplication.translate("ILTIS", "Protokolovanie Online ...", None)
        )
        self.actionPr_kazy_tla_iarne.setText(
            QCoreApplication.translate("ILTIS", "Pr\u00edkazy tla\u010diarne ...", None)
        )
        self.actionVo_ba_identifik_cie_funkcie.setText(
            QCoreApplication.translate(
                "ILTIS", "Vo\u013eba identifik\u00e1cie funkcie ...", None
            )
        )
        self.actionPrihl_senie.setText(
            QCoreApplication.translate("ILTIS", "Prihl\u00e1senie ...", None)
        )
        self.actionOdhl_senie.setText(
            QCoreApplication.translate("ILTIS", "Odhl\u00e1senie ...", None)
        )
        self.actionZavrie.setText(
            QCoreApplication.translate("ILTIS", "Zavrie\u0165 ...", None)
        )
        self.actionVo_ba_profilu.setText(
            QCoreApplication.translate("ILTIS", "Vo\u013eba profilu ...", None)
        )
        self.actionNastacvenie_zvuku.setText(
            QCoreApplication.translate("ILTIS", "Nastacvenie zvuku ...", None)
        )
        self.actionZmena_hesla.setText(
            QCoreApplication.translate("ILTIS", "Zmena hesla ...", None)
        )
        self.actionVo_ba_tla_iarne.setText(
            QCoreApplication.translate("ILTIS", "Vo\u013eba tla\u010diarne ...", None)
        )
        self.actionVo_ba_pracoviska_dr_by.setText(
            QCoreApplication.translate(
                "ILTIS", "Vo\u013eba pracoviska \u00fadr\u017eby ...", None
            )
        )
        self.actiondr_ba.setText(
            QCoreApplication.translate("ILTIS", "\u00dadr\u017eba ...", None)
        )
        self.actionTestovac_obraz_monitora.setText(
            QCoreApplication.translate(
                "ILTIS", "Testovac\u00ed obraz monitora ...", None
            )
        )
        self.actionPreh_ad.setText(
            QCoreApplication.translate("ILTIS", "Preh\u013ead ...", None)
        )
        self.actionRozsah_inform_ci.setText(
            QCoreApplication.translate("ILTIS", "Rozsah inform\u00e1ci\u00ed ...", None)
        )
        self.actionProfil.setText(
            QCoreApplication.translate("ILTIS", "Profil ...", None)
        )
        self.actionPracovisk.setText(
            QCoreApplication.translate("ILTIS", "Pracovisk\u00e1 ...", None)
        )
        self.actionIdentifik_cie_funkcie.setText(
            QCoreApplication.translate("ILTIS", "Identifik\u00e1cie funkcie ...", None)
        )
        self.actionIdentifik_cie_u_vate_a.setText(
            QCoreApplication.translate(
                "ILTIS", "Identifik\u00e1cie u\u017e\u00edvate\u013ea ...", None
            )
        )
        self.actionInfo.setText(
            QCoreApplication.translate("ILTIS", "Preh\u013ead", None)
        )
        self.actionKontext.setText(QCoreApplication.translate("ILTIS", "Kontext", None))
        self.actionVlastnosti.setText(
            QCoreApplication.translate("ILTIS", "Vlastnosti ...", None)
        )
        self.RAD_k1.setText("")
        self.RAD_k2.setText("")
        self.RAD_L1.setText("")
        self.RAD_L2.setText("")
        self.RAD_V1.setText("")
        self.RAD_fik_S.setText("")
        self.RAD_zr_do_st_odZ.setText("")
        self.RAD_Sk.setText("")
        self.RAD_zr_zo_st_odZ.setText("")
        self.RAD_ZBE_TU1.setText("")
        self.RAD_S.setText("")
        self.RAD_trat_suhlas_doZ.setText("")
        self.RAD_dialkove.setText("")
        self.RAD_ASVC.setText("")
        self.RAD_fik_29.setText("")
        self.textZbehy.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" color:#d0d0d0;">Zbehy</span></p><p><br/></p></body></html>',
                None,
            )
        )
        self.combo_hlavne.setItemText(0, "")
        self.combo_hlavne.setItemText(
            1, QCoreApplication.translate("ILTIS", "VLAK", None)
        )
        self.combo_hlavne.setItemText(
            2, QCoreApplication.translate("ILTIS", "PN", None)
        )
        self.combo_hlavne.setItemText(
            3, QCoreApplication.translate("ILTIS", "ZR JC", None)
        )
        self.combo_hlavne.setItemText(
            4, QCoreApplication.translate("ILTIS", "VOLNO", None)
        )
        self.combo_hlavne.setItemText(
            5, QCoreApplication.translate("ILTIS", "STOJ", None)
        )

        self.combo_zriad.setItemText(0, "")
        self.combo_zriad.setItemText(
            1, QCoreApplication.translate("ILTIS", "POSUN", None)
        )
        self.combo_zriad.setItemText(
            2, QCoreApplication.translate("ILTIS", "ZR JC", None)
        )
        self.combo_zriad.setItemText(
            3, QCoreApplication.translate("ILTIS", "VOLNO", None)
        )
        self.combo_zriad.setItemText(
            4, QCoreApplication.translate("ILTIS", "STOJ", None)
        )

        self.combo_vyh.setItemText(0, "")
        self.combo_vyh.setItemText(1, QCoreApplication.translate("ILTIS", "P", None))
        self.combo_vyh.setItemText(2, QCoreApplication.translate("ILTIS", "40", None))

        self.combo_kombi.setItemText(0, "")
        self.combo_kombi.setItemText(
            1, QCoreApplication.translate("ILTIS", "VLAK", None)
        )
        self.combo_kombi.setItemText(
            2, QCoreApplication.translate("ILTIS", "POSUN", None)
        )
        self.combo_kombi.setItemText(3, QCoreApplication.translate("ILTIS", "PN", None))
        self.combo_kombi.setItemText(
            4, QCoreApplication.translate("ILTIS", "ZR JC", None)
        )
        self.combo_kombi.setItemText(
            5, QCoreApplication.translate("ILTIS", "VOLNO", None)
        )
        self.combo_kombi.setItemText(
            6, QCoreApplication.translate("ILTIS", "STOJ", None)
        )

        self.RAD_1k_fik.setText("")
        self.RAD_2k_fik.setText("")
        self.textRadosina.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" font-size:18pt; font-weight:700; color:#d0d0d0;">Rado\u0161ina</span></p></body></html>',
                None,
            )
        )
        self.RAD_k2_kon.setText("")
        self.RAD_k1_kon.setText("")
        self.combo_fikt.setItemText(0, "")
        self.combo_fikt.setItemText(
            1, QCoreApplication.translate("ILTIS", "ZR JC", None)
        )

        self.combo_ciel_ko.setItemText(0, "")
        self.combo_ciel_ko.setItemText(
            1, QCoreApplication.translate("ILTIS", "PVC 40", None)
        )
        self.combo_ciel_ko.setItemText(
            2, QCoreApplication.translate("ILTIS", "PVC TR-1", None)
        )
        self.combo_ciel_ko.setItemText(
            3, QCoreApplication.translate("ILTIS", "POS-K", None)
        )

        self.combo_ciel_zr.setItemText(0, "")
        self.combo_ciel_zr.setItemText(
            1, QCoreApplication.translate("ILTIS", "POS-K", None)
        )

        self.combo_ciel_fi.setItemText(0, "")
        self.combo_ciel_fi.setItemText(
            1, QCoreApplication.translate("ILTIS", "POC", None)
        )

        self.RAD_ZBE_TU2_1.setText("")
        self.RAD_ZBE_priec.setText("")
        self.RAD_ZBE_TU2_2.setText("")
        self.combo_TS_ZBE.setItemText(0, "")
        self.combo_TS_ZBE.setItemText(
            1, QCoreApplication.translate("ILTIS", "ZUS", None)
        )
        self.combo_TS_ZBE.setItemText(
            2, QCoreApplication.translate("ILTIS", "ZR ZUS", None)
        )
        self.combo_TS_ZBE.setItemText(
            3, QCoreApplication.translate("ILTIS", "UTS", None)
        )

        self.combo_priec.setItemText(0, "")
        self.combo_priec.setItemText(
            1, QCoreApplication.translate("ILTIS", "ZATV", None)
        )
        self.combo_priec.setItemText(
            2, QCoreApplication.translate("ILTIS", "OTV", None)
        )

        self.RAD_ZBE_18.setText("")
        self.RAD_ZBE_19.setText("")
        self.combo_Riadenie.setItemText(0, "")
        self.combo_Riadenie.setItemText(
            1, QCoreApplication.translate("ILTIS", "LOKAL", None)
        )
        self.combo_Riadenie.setItemText(
            2, QCoreApplication.translate("ILTIS", "CENTR", None)
        )

        self.groupREST.setTitle(
            QCoreApplication.translate("ILTIS", "Pripojenie k REST serveru", None)
        )
        self.ButtonClose.setText(QCoreApplication.translate("ILTIS", "X", None))
        self.Line_IP.setText(
            QCoreApplication.translate("ILTIS", "158.193.224.52:8041", None)
        )
        self.ButtonConnect.setText(QCoreApplication.translate("ILTIS", "Connect", None))
        self.ButtonDisconnect.setText(
            QCoreApplication.translate("ILTIS", "Disconnect", None)
        )
        self.textConnection.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:400;">IP adresa REST API</span></p></body></html>',
                None,
            )
        )
        self.groupCentrala.setTitle(
            QCoreApplication.translate("ILTIS", "Rado\u0161ina", None)
        )
        self.groupSystem.setTitle(
            QCoreApplication.translate("ILTIS", "Syst\u00e9m:", None)
        )
        self.groupPoruchy.setTitle(
            QCoreApplication.translate("ILTIS", "Poruchy:", None)
        )
        self.textChybaREST.setText(
            QCoreApplication.translate(
                "ILTIS",
                "<html><head/><body><p>Strata spojenia s REST serverom</p><p><br/></p></body></html>",
                None,
            )
        )
        self.groupHlasenia.setTitle(
            QCoreApplication.translate(
                "ILTIS", "Prev\u00e1dzkov\u00e9 hl\u00e1senia:", None
            )
        )
        self.groupHlasenia_2.setTitle(
            QCoreApplication.translate("ILTIS", "V\u00fdzvy pre obsluhu:", None)
        )
        self.DateTime.setText(
            QCoreApplication.translate("ILTIS", "01.01.1970 00:00:00", None)
        )
        self.groupPrehlad.setTitle(
            QCoreApplication.translate("ILTIS", "Preh\u013ead", None)
        )
        self.label_4.setText(QCoreApplication.translate("ILTIS", "obsluhy", None))
        self.ButtonClose_1.setText(QCoreApplication.translate("ILTIS", "X", None))
        self.label_5.setText(QCoreApplication.translate("ILTIS", "Verzia 1.1", None))
        self.label_6.setText(
            QCoreApplication.translate("ILTIS", "ILTIS-N Rado\u0161ina", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("ILTIS", "D\u00e1vid Macko", None)
        )
        self.label_8.setText(QCoreApplication.translate("ILTIS", "2024", None))
        self.label_9.setText(
            QCoreApplication.translate("ILTIS", "Pracovisko lok\u00e1lnej", None)
        )
        self.menuSyst_m.setTitle(
            QCoreApplication.translate("ILTIS", "Syst\u00e9m", None)
        )
        self.menuSpr_va_hl_sen.setTitle(
            QCoreApplication.translate("ILTIS", "Spr\u00e1va hl\u00e1sen\u00ed", None)
        )
        self.menu_V_RD.setTitle(QCoreApplication.translate("ILTIS", "\u010cV/RD", None))
        self.menuKonfigur_cia.setTitle(
            QCoreApplication.translate("ILTIS", "Konfigur\u00e1cia", None)
        )
        self.menuSpr_va_syst_mu.setTitle(
            QCoreApplication.translate("ILTIS", "Spr\u00e1va syst\u00e9mu", None)
        )
        self.menuPomoc.setTitle(QCoreApplication.translate("ILTIS", "Pomoc", None))
        self.menuREST_server.setTitle(
            QCoreApplication.translate("ILTIS", "REST server", None)
        )

    # retranslateUi
