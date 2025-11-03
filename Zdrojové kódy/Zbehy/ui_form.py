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
        self.actionVlastnosti = QAction(ILTIS)
        self.actionVlastnosti.setObjectName("actionVlastnosti")
        self.actionVo_ba_rozsahu_inform_ci = QAction(ILTIS)
        self.actionVo_ba_rozsahu_inform_ci.setObjectName(
            "actionVo_ba_rozsahu_inform_ci"
        )
        self.actionAlarm_vypn = QAction(ILTIS)
        self.actionAlarm_vypn.setObjectName("actionAlarm_vypn")
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
        self.actionHorizont_lne = QAction(ILTIS)
        self.actionHorizont_lne.setObjectName("actionHorizont_lne")
        self.actionVertik_lne = QAction(ILTIS)
        self.actionVertik_lne.setObjectName("actionVertik_lne")
        self.actionVo_ba_profilu = QAction(ILTIS)
        self.actionVo_ba_profilu.setObjectName("actionVo_ba_profilu")
        self.actionNastavenie_zvuku = QAction(ILTIS)
        self.actionNastavenie_zvuku.setObjectName("actionNastavenie_zvuku")
        self.actionZmena_hesla = QAction(ILTIS)
        self.actionZmena_hesla.setObjectName("actionZmena_hesla")
        self.actionVo_ba_tla_iarne = QAction(ILTIS)
        self.actionVo_ba_tla_iarne.setObjectName("actionVo_ba_tla_iarne")
        self.actionVo_ba_pracoviska_dr_by = QAction(ILTIS)
        self.actionVo_ba_pracoviska_dr_by.setObjectName("actionVo_ba_pracoviska_dr_by")
        self.action_dr_ba = QAction(ILTIS)
        self.action_dr_ba.setObjectName("action_dr_ba")
        self.actionTestovac_obraz_monitora = QAction(ILTIS)
        self.actionTestovac_obraz_monitora.setObjectName(
            "actionTestovac_obraz_monitora"
        )
        self.actionPreh_ad = QAction(ILTIS)
        self.actionPreh_ad.setObjectName("actionPreh_ad")
        self.actionRozsah_nform_ci = QAction(ILTIS)
        self.actionRozsah_nform_ci.setObjectName("actionRozsah_nform_ci")
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
        self.centralwidget = QWidget(ILTIS)
        self.centralwidget.setObjectName("centralwidget")
        self.RAD_ZBE_TU4 = QPushButton(self.centralwidget)
        self.RAD_ZBE_TU4.setObjectName("RAD_ZBE_TU4")
        self.RAD_ZBE_TU4.setGeometry(QRect(367, 298, 125, 59))
        icon = QIcon()
        icon.addFile("img/Kolaj/Kol_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.RAD_ZBE_TU4.setIcon(icon)
        self.RAD_ZBE_TU4.setIconSize(QSize(125, 59))
        self.RAD_ZBE_TU4.setAutoDefault(False)
        self.RAD_ZBE_TU4.setFlat(False)
        self.ZBE_L = QPushButton(self.centralwidget)
        self.ZBE_L.setObjectName("ZBE_L")
        self.ZBE_L.setGeometry(QRect(492, 300, 38, 58))
        icon1 = QIcon()
        icon1.addFile("img/HlavneNav/Hl_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_L.setIcon(icon1)
        self.ZBE_L.setIconSize(QSize(38, 58))
        self.ZBE_L.setAutoDefault(False)
        self.ZBE_L.setFlat(False)
        self.ZBE_fik_L = QPushButton(self.centralwidget)
        self.ZBE_fik_L.setObjectName("ZBE_fik_L")
        self.ZBE_fik_L.setGeometry(QRect(530, 308, 24, 43))
        icon2 = QIcon()
        icon2.addFile("img/Fiktivne/Fikt_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_fik_L.setIcon(icon2)
        self.ZBE_fik_L.setIconSize(QSize(24, 43))
        self.ZBE_fik_L.setAutoDefault(False)
        self.ZBE_fik_L.setFlat(False)
        self.ZBE_zr_zo_st_odR = QPushButton(self.centralwidget)
        self.ZBE_zr_zo_st_odR.setObjectName("ZBE_zr_zo_st_odR")
        self.ZBE_zr_zo_st_odR.setGeometry(QRect(554, 308, 23, 43))
        icon3 = QIcon()
        icon3.addFile("img/Zriad/Zriad_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_zr_zo_st_odR.setIcon(icon3)
        self.ZBE_zr_zo_st_odR.setIconSize(QSize(23, 43))
        self.ZBE_zr_zo_st_odR.setAutoDefault(False)
        self.ZBE_zr_zo_st_odR.setFlat(False)
        self.ZBE_k1L = QPushButton(self.centralwidget)
        self.ZBE_k1L.setObjectName("ZBE_k1L")
        self.ZBE_k1L.setGeometry(QRect(577, 299, 125, 59))
        self.ZBE_k1L.setIcon(icon)
        self.ZBE_k1L.setIconSize(QSize(125, 59))
        self.ZBE_k1L.setAutoDefault(False)
        self.ZBE_k1L.setFlat(False)
        self.ZBE_zr_do_st_odR = QPushButton(self.centralwidget)
        self.ZBE_zr_do_st_odR.setObjectName("ZBE_zr_do_st_odR")
        self.ZBE_zr_do_st_odR.setGeometry(QRect(702, 308, 23, 43))
        icon4 = QIcon()
        icon4.addFile("img/Zriad/Zriad_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_zr_do_st_odR.setIcon(icon4)
        self.ZBE_zr_do_st_odR.setIconSize(QSize(23, 43))
        self.ZBE_zr_do_st_odR.setAutoDefault(False)
        self.ZBE_zr_do_st_odR.setFlat(False)
        self.ZBE_V1 = QPushButton(self.centralwidget)
        self.ZBE_V1.setObjectName("ZBE_V1")
        self.ZBE_V1.setGeometry(QRect(725, 300, 125, 57))
        icon5 = QIcon()
        icon5.addFile(
            "img/VyhSpojka/Spojka_basic_A.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.ZBE_V1.setIcon(icon5)
        self.ZBE_V1.setIconSize(QSize(125, 57))
        self.ZBE_V1.setAutoDefault(False)
        self.ZBE_V1.setFlat(False)
        self.ZBE_V2 = QPushButton(self.centralwidget)
        self.ZBE_V2.setObjectName("ZBE_V2")
        self.ZBE_V2.setGeometry(QRect(725, 357, 125, 55))
        icon6 = QIcon()
        icon6.addFile(
            "img/VyhSpojka/Spojka_basic_B.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.ZBE_V2.setIcon(icon6)
        self.ZBE_V2.setIconSize(QSize(125, 55))
        self.ZBE_V2.setAutoDefault(False)
        self.ZBE_V2.setFlat(False)
        self.ZBE_S1 = QPushButton(self.centralwidget)
        self.ZBE_S1.setObjectName("ZBE_S1")
        self.ZBE_S1.setGeometry(QRect(850, 301, 52, 58))
        icon7 = QIcon()
        icon7.addFile(
            "img/HlavneKombinovaneNav/Kom_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.ZBE_S1.setIcon(icon7)
        self.ZBE_S1.setIconSize(QSize(52, 58))
        self.ZBE_S1.setAutoDefault(False)
        self.ZBE_S1.setFlat(False)
        self.ZBE_S2 = QPushButton(self.centralwidget)
        self.ZBE_S2.setObjectName("ZBE_S2")
        self.ZBE_S2.setGeometry(QRect(850, 359, 52, 58))
        self.ZBE_S2.setIcon(icon7)
        self.ZBE_S2.setIconSize(QSize(68, 59))
        self.ZBE_S2.setAutoDefault(False)
        self.ZBE_S2.setFlat(False)
        self.ZBE_k1 = QPushButton(self.centralwidget)
        self.ZBE_k1.setObjectName("ZBE_k1")
        self.ZBE_k1.setGeometry(QRect(902, 300, 125, 59))
        icon8 = QIcon()
        icon8.addFile("img/Kolaj/Kol_st1_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_k1.setIcon(icon8)
        self.ZBE_k1.setIconSize(QSize(125, 59))
        self.ZBE_k1.setAutoDefault(False)
        self.ZBE_k1.setFlat(False)
        self.ZBE_k2 = QPushButton(self.centralwidget)
        self.ZBE_k2.setObjectName("ZBE_k2")
        self.ZBE_k2.setGeometry(QRect(902, 358, 125, 59))
        icon9 = QIcon()
        icon9.addFile("img/Kolaj/Kol_st2_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_k2.setIcon(icon9)
        self.ZBE_k2.setIconSize(QSize(125, 59))
        self.ZBE_k2.setAutoDefault(False)
        self.ZBE_k2.setFlat(False)
        self.ZBE_L1 = QPushButton(self.centralwidget)
        self.ZBE_L1.setObjectName("ZBE_L1")
        self.ZBE_L1.setGeometry(QRect(1027, 301, 52, 58))
        icon10 = QIcon()
        icon10.addFile(
            "img/HlavneKombinovaneNav/Kom_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.ZBE_L1.setIcon(icon10)
        self.ZBE_L1.setIconSize(QSize(68, 59))
        self.ZBE_L1.setAutoDefault(False)
        self.ZBE_L1.setFlat(False)
        self.ZBE_L2 = QPushButton(self.centralwidget)
        self.ZBE_L2.setObjectName("ZBE_L2")
        self.ZBE_L2.setGeometry(QRect(1027, 359, 52, 58))
        self.ZBE_L2.setIcon(icon10)
        self.ZBE_L2.setIconSize(QSize(68, 59))
        self.ZBE_L2.setAutoDefault(False)
        self.ZBE_L2.setFlat(False)
        self.ZBE_V3 = QPushButton(self.centralwidget)
        self.ZBE_V3.setObjectName("ZBE_V3")
        self.ZBE_V3.setGeometry(QRect(1079, 300, 125, 117))
        icon11 = QIcon()
        icon11.addFile("img/Vyhybka/VyhPH_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_V3.setIcon(icon11)
        self.ZBE_V3.setIconSize(QSize(125, 117))
        self.ZBE_V3.setAutoDefault(False)
        self.ZBE_V3.setFlat(False)
        self.ZBE_fik_S = QPushButton(self.centralwidget)
        self.ZBE_fik_S.setObjectName("ZBE_fik_S")
        self.ZBE_fik_S.setGeometry(QRect(1375, 307, 24, 43))
        icon12 = QIcon()
        icon12.addFile("img/Fiktivne/Fikt_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_fik_S.setIcon(icon12)
        self.ZBE_fik_S.setIconSize(QSize(24, 43))
        self.ZBE_fik_S.setAutoDefault(False)
        self.ZBE_fik_S.setFlat(False)
        self.ZBE_zr_do_st_odH = QPushButton(self.centralwidget)
        self.ZBE_zr_do_st_odH.setObjectName("ZBE_zr_do_st_odH")
        self.ZBE_zr_do_st_odH.setGeometry(QRect(1204, 308, 23, 43))
        self.ZBE_zr_do_st_odH.setIcon(icon3)
        self.ZBE_zr_do_st_odH.setIconSize(QSize(68, 59))
        self.ZBE_zr_do_st_odH.setAutoDefault(False)
        self.ZBE_zr_do_st_odH.setFlat(False)
        self.ZBE_k1S = QPushButton(self.centralwidget)
        self.ZBE_k1S.setObjectName("ZBE_k1S")
        self.ZBE_k1S.setGeometry(QRect(1227, 299, 125, 59))
        self.ZBE_k1S.setIcon(icon)
        self.ZBE_k1S.setIconSize(QSize(125, 59))
        self.ZBE_k1S.setAutoDefault(False)
        self.ZBE_k1S.setFlat(False)
        self.ZBE_zr_zo_st_odH = QPushButton(self.centralwidget)
        self.ZBE_zr_zo_st_odH.setObjectName("ZBE_zr_zo_st_odH")
        self.ZBE_zr_zo_st_odH.setGeometry(QRect(1352, 308, 23, 43))
        self.ZBE_zr_zo_st_odH.setIcon(icon4)
        self.ZBE_zr_zo_st_odH.setIconSize(QSize(68, 59))
        self.ZBE_zr_zo_st_odH.setAutoDefault(False)
        self.ZBE_zr_zo_st_odH.setFlat(False)
        self.ZBE_trat_suhlas_doR = QPushButton(self.centralwidget)
        self.ZBE_trat_suhlas_doR.setObjectName("ZBE_trat_suhlas_doR")
        self.ZBE_trat_suhlas_doR.setGeometry(QRect(451, 281, 39, 18))
        icon13 = QIcon()
        icon13.addFile("img/TS/TS_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_trat_suhlas_doR.setIcon(icon13)
        self.ZBE_trat_suhlas_doR.setIconSize(QSize(39, 18))
        self.ZBE_trat_suhlas_doR.setAutoDefault(False)
        self.ZBE_trat_suhlas_doR.setFlat(False)
        self.ZBE_zr_do_st_odL = QPushButton(self.centralwidget)
        self.ZBE_zr_do_st_odL.setObjectName("ZBE_zr_do_st_odL")
        self.ZBE_zr_do_st_odL.setGeometry(QRect(702, 366, 23, 43))
        self.ZBE_zr_do_st_odL.setIcon(icon4)
        self.ZBE_zr_do_st_odL.setIconSize(QSize(23, 43))
        self.ZBE_zr_do_st_odL.setAutoDefault(False)
        self.ZBE_zr_do_st_odL.setFlat(False)
        self.ZBE_zr_zo_st_odL = QPushButton(self.centralwidget)
        self.ZBE_zr_zo_st_odL.setObjectName("ZBE_zr_zo_st_odL")
        self.ZBE_zr_zo_st_odL.setGeometry(QRect(554, 366, 23, 43))
        self.ZBE_zr_zo_st_odL.setIcon(icon3)
        self.ZBE_zr_zo_st_odL.setIconSize(QSize(23, 43))
        self.ZBE_zr_zo_st_odL.setAutoDefault(False)
        self.ZBE_zr_zo_st_odL.setFlat(False)
        self.ZBE_BL = QPushButton(self.centralwidget)
        self.ZBE_BL.setObjectName("ZBE_BL")
        self.ZBE_BL.setGeometry(QRect(492, 358, 38, 58))
        self.ZBE_BL.setIcon(icon1)
        self.ZBE_BL.setIconSize(QSize(38, 58))
        self.ZBE_BL.setAutoDefault(False)
        self.ZBE_BL.setFlat(False)
        self.ZBE_trat_suhlas_doL = QPushButton(self.centralwidget)
        self.ZBE_trat_suhlas_doL.setObjectName("ZBE_trat_suhlas_doL")
        self.ZBE_trat_suhlas_doL.setGeometry(QRect(451, 415, 39, 18))
        self.ZBE_trat_suhlas_doL.setIcon(icon13)
        self.ZBE_trat_suhlas_doL.setIconSize(QSize(39, 18))
        self.ZBE_trat_suhlas_doL.setAutoDefault(False)
        self.ZBE_trat_suhlas_doL.setFlat(False)
        self.ZBE_k2BL = QPushButton(self.centralwidget)
        self.ZBE_k2BL.setObjectName("ZBE_k2BL")
        self.ZBE_k2BL.setGeometry(QRect(577, 357, 125, 59))
        self.ZBE_k2BL.setIcon(icon)
        self.ZBE_k2BL.setIconSize(QSize(125, 59))
        self.ZBE_k2BL.setAutoDefault(False)
        self.ZBE_k2BL.setFlat(False)
        self.ZBE_fik_BL = QPushButton(self.centralwidget)
        self.ZBE_fik_BL.setObjectName("ZBE_fik_BL")
        self.ZBE_fik_BL.setGeometry(QRect(530, 366, 24, 43))
        self.ZBE_fik_BL.setIcon(icon2)
        self.ZBE_fik_BL.setIconSize(QSize(24, 43))
        self.ZBE_fik_BL.setAutoDefault(False)
        self.ZBE_fik_BL.setFlat(False)
        self.textLuzianky = QLabel(self.centralwidget)
        self.textLuzianky.setObjectName("textLuzianky")
        self.textLuzianky.setGeometry(QRect(234, 365, 101, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.textLuzianky.setFont(font)
        self.textLuzianky.setTextFormat(Qt.AutoText)
        self.textLuzianky.setScaledContents(True)
        self.ZBE_HLO_TU1_1 = QPushButton(self.centralwidget)
        self.ZBE_HLO_TU1_1.setObjectName("ZBE_HLO_TU1_1")
        self.ZBE_HLO_TU1_1.setGeometry(QRect(1437, 298, 125, 59))
        self.ZBE_HLO_TU1_1.setIcon(icon)
        self.ZBE_HLO_TU1_1.setIconSize(QSize(125, 59))
        self.ZBE_HLO_TU1_1.setAutoDefault(False)
        self.ZBE_HLO_TU1_1.setFlat(False)
        self.ZBE_S = QPushButton(self.centralwidget)
        self.ZBE_S.setObjectName("ZBE_S")
        self.ZBE_S.setGeometry(QRect(1399, 300, 38, 58))
        icon14 = QIcon()
        icon14.addFile("img/HlavneNav/Hl_basicL.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_S.setIcon(icon14)
        self.ZBE_S.setIconSize(QSize(38, 58))
        self.ZBE_S.setAutoDefault(False)
        self.ZBE_S.setFlat(False)
        self.ZBE_trat_suhlas_doH = QPushButton(self.centralwidget)
        self.ZBE_trat_suhlas_doH.setObjectName("ZBE_trat_suhlas_doH")
        self.ZBE_trat_suhlas_doH.setGeometry(QRect(1445, 354, 39, 18))
        icon15 = QIcon()
        icon15.addFile("img/TS/TS_basicP.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_trat_suhlas_doH.setIcon(icon15)
        self.ZBE_trat_suhlas_doH.setIconSize(QSize(39, 18))
        self.ZBE_trat_suhlas_doH.setAutoDefault(False)
        self.ZBE_trat_suhlas_doH.setFlat(False)
        self.ZBE_dialkove = QPushButton(self.centralwidget)
        self.ZBE_dialkove.setObjectName("ZBE_dialkove")
        self.ZBE_dialkove.setGeometry(QRect(930, 230, 58, 43))
        icon16 = QIcon()
        icon16.addFile("img/Stanice/ZBE_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_dialkove.setIcon(icon16)
        self.ZBE_dialkove.setIconSize(QSize(58, 43))
        self.ZBE_ASVC = QPushButton(self.centralwidget)
        self.ZBE_ASVC.setObjectName("ZBE_ASVC")
        self.ZBE_ASVC.setGeometry(QRect(990, 230, 58, 43))
        icon17 = QIcon()
        icon17.addFile("img/Stanice/ASVC_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.ZBE_ASVC.setIcon(icon17)
        self.ZBE_ASVC.setIconSize(QSize(58, 43))
        self.RAD_ZBE_fik_28 = QPushButton(self.centralwidget)
        self.RAD_ZBE_fik_28.setObjectName("RAD_ZBE_fik_28")
        self.RAD_ZBE_fik_28.setGeometry(QRect(142, 310, 24, 37))
        self.RAD_ZBE_fik_28.setIcon(icon2)
        self.RAD_ZBE_fik_28.setIconSize(QSize(24, 43))
        self.RAD_ZBE_fik_28.setAutoDefault(False)
        self.RAD_ZBE_fik_28.setFlat(False)
        self.HLO_fiktL = QPushButton(self.centralwidget)
        self.HLO_fiktL.setObjectName("HLO_fiktL")
        self.HLO_fiktL.setGeometry(QRect(1762, 306, 24, 43))
        self.HLO_fiktL.setIcon(icon12)
        self.HLO_fiktL.setIconSize(QSize(24, 43))
        self.HLO_fiktL.setAutoDefault(False)
        self.HLO_fiktL.setFlat(False)
        self.textRadosina = QLabel(self.centralwidget)
        self.textRadosina.setObjectName("textRadosina")
        self.textRadosina.setGeometry(QRect(30, 310, 111, 41))
        self.textRadosina.setFont(font)
        self.textRadosina.setTextFormat(Qt.AutoText)
        self.textRadosina.setScaledContents(True)
        self.textHlohovec = QLabel(self.centralwidget)
        self.textHlohovec.setObjectName("textHlohovec")
        self.textHlohovec.setGeometry(QRect(1790, 310, 121, 41))
        self.textHlohovec.setFont(font)
        self.textHlohovec.setTextFormat(Qt.AutoText)
        self.textHlohovec.setScaledContents(True)
        self.ZBE_pracovisko = QLabel(self.centralwidget)
        self.ZBE_pracovisko.setObjectName("ZBE_pracovisko")
        self.ZBE_pracovisko.setGeometry(QRect(860, 230, 55, 38))
        self.ZBE_pracovisko.setFont(font)
        self.ZBE_pracovisko.setTextFormat(Qt.AutoText)
        self.ZBE_pracovisko.setPixmap(QPixmap("img/Stanice/Pracovisko.bmp"))
        self.ZBE_pracovisko.setScaledContents(True)
        self.combo_hlavne = QComboBox(self.centralwidget)
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.addItem("")
        self.combo_hlavne.setObjectName("combo_hlavne")
        self.combo_hlavne.setGeometry(QRect(880, 430, 72, 24))
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
        self.combo_zriad.setGeometry(QRect(880, 430, 72, 24))
        self.combo_zriad.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_vyh = QComboBox(self.centralwidget)
        self.combo_vyh.addItem("")
        self.combo_vyh.addItem("")
        self.combo_vyh.setObjectName("combo_vyh")
        self.combo_vyh.setGeometry(QRect(953, 430, 72, 24))
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
        self.combo_kombi.setGeometry(QRect(880, 430, 72, 24))
        self.combo_kombi.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_ciel_fi = QComboBox(self.centralwidget)
        self.combo_ciel_fi.addItem("")
        self.combo_ciel_fi.addItem("")
        self.combo_ciel_fi.setObjectName("combo_ciel_fi")
        self.combo_ciel_fi.setGeometry(QRect(880, 455, 72, 24))
        self.combo_ciel_fi.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_fikt = QComboBox(self.centralwidget)
        self.combo_fikt.addItem("")
        self.combo_fikt.addItem("")
        self.combo_fikt.setObjectName("combo_fikt")
        self.combo_fikt.setGeometry(QRect(880, 430, 72, 24))
        self.combo_fikt.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_ciel_zr = QComboBox(self.centralwidget)
        self.combo_ciel_zr.addItem("")
        self.combo_ciel_zr.addItem("")
        self.combo_ciel_zr.setObjectName("combo_ciel_zr")
        self.combo_ciel_zr.setGeometry(QRect(880, 455, 72, 24))
        self.combo_ciel_zr.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_ciel_ko = QComboBox(self.centralwidget)
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.addItem("")
        self.combo_ciel_ko.setObjectName("combo_ciel_ko")
        self.combo_ciel_ko.setGeometry(QRect(880, 455, 72, 24))
        self.combo_ciel_ko.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_TS_RAD = QComboBox(self.centralwidget)
        self.combo_TS_RAD.addItem("")
        self.combo_TS_RAD.addItem("")
        self.combo_TS_RAD.addItem("")
        self.combo_TS_RAD.addItem("")
        self.combo_TS_RAD.setObjectName("combo_TS_RAD")
        self.combo_TS_RAD.setGeometry(QRect(430, 250, 72, 24))
        self.combo_TS_RAD.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_TS_HLO = QComboBox(self.centralwidget)
        self.combo_TS_HLO.addItem("")
        self.combo_TS_HLO.addItem("")
        self.combo_TS_HLO.setObjectName("combo_TS_HLO")
        self.combo_TS_HLO.setGeometry(QRect(1430, 380, 72, 24))
        self.combo_TS_HLO.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.combo_TS_LUZ = QComboBox(self.centralwidget)
        self.combo_TS_LUZ.addItem("")
        self.combo_TS_LUZ.addItem("")
        self.combo_TS_LUZ.addItem("")
        self.combo_TS_LUZ.addItem("")
        self.combo_TS_LUZ.addItem("")
        self.combo_TS_LUZ.setObjectName("combo_TS_LUZ")
        self.combo_TS_LUZ.setGeometry(QRect(430, 440, 72, 24))
        self.combo_TS_LUZ.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
        )
        self.RAD_ZBE_TU3 = QPushButton(self.centralwidget)
        self.RAD_ZBE_TU3.setObjectName("RAD_ZBE_TU3")
        self.RAD_ZBE_TU3.setGeometry(QRect(166, 298, 125, 59))
        self.RAD_ZBE_TU3.setIcon(icon)
        self.RAD_ZBE_TU3.setIconSize(QSize(125, 59))
        self.RAD_ZBE_TU3.setAutoDefault(False)
        self.RAD_ZBE_TU3.setFlat(False)
        self.RAD_ZBE_39 = QPushButton(self.centralwidget)
        self.RAD_ZBE_39.setObjectName("RAD_ZBE_39")
        self.RAD_ZBE_39.setGeometry(QRect(291, 300, 38, 58))
        self.RAD_ZBE_39.setIcon(icon1)
        self.RAD_ZBE_39.setIconSize(QSize(38, 58))
        self.RAD_ZBE_39.setAutoDefault(False)
        self.RAD_ZBE_39.setFlat(False)
        self.RAD_ZBE_40 = QPushButton(self.centralwidget)
        self.RAD_ZBE_40.setObjectName("RAD_ZBE_40")
        self.RAD_ZBE_40.setGeometry(QRect(329, 300, 38, 58))
        self.RAD_ZBE_40.setIcon(icon14)
        self.RAD_ZBE_40.setIconSize(QSize(38, 58))
        self.RAD_ZBE_40.setAutoDefault(False)
        self.RAD_ZBE_40.setFlat(False)
        self.ZBE_HLO_TU2_a = QPushButton(self.centralwidget)
        self.ZBE_HLO_TU2_a.setObjectName("ZBE_HLO_TU2_a")
        self.ZBE_HLO_TU2_a.setGeometry(QRect(1638, 297, 51, 59))
        self.ZBE_HLO_TU2_a.setIcon(icon)
        self.ZBE_HLO_TU2_a.setIconSize(QSize(125, 59))
        self.ZBE_HLO_TU2_a.setAutoDefault(False)
        self.ZBE_HLO_TU2_a.setFlat(False)
        self.ZBE_HLO_So = QPushButton(self.centralwidget)
        self.ZBE_HLO_So.setObjectName("ZBE_HLO_So")
        self.ZBE_HLO_So.setGeometry(QRect(1600, 299, 38, 58))
        self.ZBE_HLO_So.setIcon(icon14)
        self.ZBE_HLO_So.setIconSize(QSize(38, 58))
        self.ZBE_HLO_So.setAutoDefault(False)
        self.ZBE_HLO_So.setFlat(False)
        self.ZBE_HLO_Lo = QPushButton(self.centralwidget)
        self.ZBE_HLO_Lo.setObjectName("ZBE_HLO_Lo")
        self.ZBE_HLO_Lo.setGeometry(QRect(1562, 300, 38, 58))
        self.ZBE_HLO_Lo.setIcon(icon1)
        self.ZBE_HLO_Lo.setIconSize(QSize(38, 58))
        self.ZBE_HLO_Lo.setAutoDefault(False)
        self.ZBE_HLO_Lo.setFlat(False)
        self.ZBE_HLO_TU2_b = QPushButton(self.centralwidget)
        self.ZBE_HLO_TU2_b.setObjectName("ZBE_HLO_TU2_b")
        self.ZBE_HLO_TU2_b.setGeometry(QRect(1711, 297, 51, 59))
        self.ZBE_HLO_TU2_b.setIcon(icon)
        self.ZBE_HLO_TU2_b.setIconSize(QSize(125, 59))
        self.ZBE_HLO_TU2_b.setAutoDefault(False)
        self.ZBE_HLO_TU2_b.setFlat(False)
        self.ZBE_HLO_priec = QPushButton(self.centralwidget)
        self.ZBE_HLO_priec.setObjectName("ZBE_HLO_priec")
        self.ZBE_HLO_priec.setGeometry(QRect(1689, 302, 22, 53))
        icon18 = QIcon()
        icon18.addFile(
            "img/Priecestie/Priec_basic.bmp", QSize(), QIcon.Normal, QIcon.Off
        )
        self.ZBE_HLO_priec.setIcon(icon18)
        self.ZBE_HLO_priec.setIconSize(QSize(22, 53))
        self.ZBE_HLO_priec.setAutoDefault(False)
        self.ZBE_HLO_priec.setFlat(False)
        self.textZbehy = QLabel(self.centralwidget)
        self.textZbehy.setObjectName("textZbehy")
        self.textZbehy.setGeometry(QRect(910, 170, 121, 41))
        self.textZbehy.setFont(font)
        self.textZbehy.setTextFormat(Qt.AutoText)
        self.textZbehy.setScaledContents(True)
        self.combo_oddielove = QComboBox(self.centralwidget)
        self.combo_oddielove.addItem("")
        self.combo_oddielove.addItem("")
        self.combo_oddielove.addItem("")
        self.combo_oddielove.addItem("")
        self.combo_oddielove.setObjectName("combo_oddielove")
        self.combo_oddielove.setGeometry(QRect(880, 430, 72, 24))
        self.combo_oddielove.setStyleSheet(
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
        self.textChybaESA = QLabel(self.groupPoruchy)
        self.textChybaESA.setObjectName("textChybaESA")
        self.textChybaESA.setGeometry(QRect(15, 30, 261, 21))
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.textChybaESA.setFont(font2)
        self.textChybaESA.setStyleSheet("color: rgb(166, 166, 166);")
        self.textChybaESA.setTextFormat(Qt.AutoText)
        self.textChybaESA.setScaledContents(True)
        self.textChybaREST = QLabel(self.groupPoruchy)
        self.textChybaREST.setObjectName("textChybaREST")
        self.textChybaREST.setGeometry(QRect(15, 50, 261, 21))
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
        self.combo_Riadenie = QComboBox(self.centralwidget)
        self.combo_Riadenie.addItem("")
        self.combo_Riadenie.addItem("")
        self.combo_Riadenie.addItem("")
        self.combo_Riadenie.setObjectName("combo_Riadenie")
        self.combo_Riadenie.setGeometry(QRect(953, 455, 72, 24))
        self.combo_Riadenie.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
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
        self.LUZ_ZBE_TU1 = QPushButton(self.centralwidget)
        self.LUZ_ZBE_TU1.setObjectName("LUZ_ZBE_TU1")
        self.LUZ_ZBE_TU1.setGeometry(QRect(367, 356, 125, 59))
        self.LUZ_ZBE_TU1.setIcon(icon)
        self.LUZ_ZBE_TU1.setIconSize(QSize(125, 59))
        self.LUZ_ZBE_TU1.setAutoDefault(False)
        self.LUZ_ZBE_TU1.setFlat(False)
        self.LUZ_fik_BS = QPushButton(self.centralwidget)
        self.LUZ_fik_BS.setObjectName("LUZ_fik_BS")
        self.LUZ_fik_BS.setGeometry(QRect(343, 368, 24, 37))
        self.LUZ_fik_BS.setIcon(icon2)
        self.LUZ_fik_BS.setIconSize(QSize(24, 43))
        self.LUZ_fik_BS.setAutoDefault(False)
        self.LUZ_fik_BS.setFlat(False)
        ILTIS.setCentralWidget(self.centralwidget)
        self.ZBE_k2.raise_()
        self.RAD_ZBE_TU4.raise_()
        self.ZBE_L.raise_()
        self.ZBE_fik_L.raise_()
        self.ZBE_zr_zo_st_odR.raise_()
        self.ZBE_k1L.raise_()
        self.ZBE_zr_do_st_odR.raise_()
        self.ZBE_V2.raise_()
        self.ZBE_V1.raise_()
        self.ZBE_S1.raise_()
        self.ZBE_S2.raise_()
        self.ZBE_L1.raise_()
        self.ZBE_L2.raise_()
        self.ZBE_V3.raise_()
        self.ZBE_k1.raise_()
        self.ZBE_fik_S.raise_()
        self.ZBE_zr_do_st_odH.raise_()
        self.ZBE_k1S.raise_()
        self.ZBE_zr_zo_st_odH.raise_()
        self.ZBE_trat_suhlas_doR.raise_()
        self.ZBE_zr_do_st_odL.raise_()
        self.ZBE_zr_zo_st_odL.raise_()
        self.ZBE_BL.raise_()
        self.ZBE_trat_suhlas_doL.raise_()
        self.ZBE_k2BL.raise_()
        self.ZBE_fik_BL.raise_()
        self.textLuzianky.raise_()
        self.ZBE_HLO_TU1_1.raise_()
        self.ZBE_S.raise_()
        self.ZBE_trat_suhlas_doH.raise_()
        self.ZBE_dialkove.raise_()
        self.ZBE_ASVC.raise_()
        self.RAD_ZBE_fik_28.raise_()
        self.HLO_fiktL.raise_()
        self.textRadosina.raise_()
        self.textHlohovec.raise_()
        self.ZBE_pracovisko.raise_()
        self.combo_hlavne.raise_()
        self.combo_zriad.raise_()
        self.combo_vyh.raise_()
        self.combo_kombi.raise_()
        self.combo_ciel_fi.raise_()
        self.combo_fikt.raise_()
        self.combo_ciel_zr.raise_()
        self.combo_ciel_ko.raise_()
        self.combo_TS_RAD.raise_()
        self.combo_TS_HLO.raise_()
        self.combo_TS_LUZ.raise_()
        self.RAD_ZBE_TU3.raise_()
        self.RAD_ZBE_39.raise_()
        self.RAD_ZBE_40.raise_()
        self.ZBE_HLO_TU2_a.raise_()
        self.ZBE_HLO_So.raise_()
        self.ZBE_HLO_Lo.raise_()
        self.ZBE_HLO_TU2_b.raise_()
        self.ZBE_HLO_priec.raise_()
        self.textZbehy.raise_()
        self.combo_oddielove.raise_()
        self.groupREST.raise_()
        self.groupCentrala.raise_()
        self.DateTime.raise_()
        self.combo_Riadenie.raise_()
        self.groupPrehlad.raise_()
        self.LUZ_ZBE_TU1.raise_()
        self.LUZ_fik_BS.raise_()
        self.menubar = QMenuBar(ILTIS)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 21))
        self.menubar.setStyleSheet(
            "color: rgb(0, 0, 0);\n" "background-color: rgb(166, 166, 166);"
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
        self.menuSyst_m.addAction(self.actionVo_ba_rozsahu_inform_ci)
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
        self.menuKonfigur_cia.addAction(self.actionNastavenie_zvuku)
        self.menuKonfigur_cia.addAction(self.actionZmena_hesla)
        self.menuKonfigur_cia.addAction(self.actionVo_ba_tla_iarne)
        self.menuKonfigur_cia.addSeparator()
        self.menuKonfigur_cia.addAction(self.menuSpr_va_syst_mu.menuAction())
        self.menuKonfigur_cia.addSeparator()
        self.menuKonfigur_cia.addAction(self.actionVo_ba_pracoviska_dr_by)
        self.menuKonfigur_cia.addAction(self.action_dr_ba)
        self.menuKonfigur_cia.addAction(self.actionTestovac_obraz_monitora)
        self.menuKonfigur_cia.addSeparator()
        self.menuKonfigur_cia.addAction(self.actionPreh_ad)
        self.menuSpr_va_syst_mu.addAction(self.actionRozsah_nform_ci)
        self.menuSpr_va_syst_mu.addAction(self.actionProfil)
        self.menuSpr_va_syst_mu.addAction(self.actionPracovisk)
        self.menuSpr_va_syst_mu.addAction(self.actionIdentifik_cie_funkcie)
        self.menuSpr_va_syst_mu.addAction(self.actionIdentifik_cie_u_vate_a)
        self.menuPomoc.addAction(self.actionInfo)
        self.menuPomoc.addAction(self.actionKontext)
        self.menuREST_server.addAction(self.actionVlastnosti)

        self.retranslateUi(ILTIS)

        self.RAD_ZBE_TU4.setDefault(False)
        self.ZBE_L.setDefault(False)
        self.ZBE_fik_L.setDefault(False)
        self.ZBE_zr_zo_st_odR.setDefault(False)
        self.ZBE_k1L.setDefault(False)
        self.ZBE_zr_do_st_odR.setDefault(False)
        self.ZBE_V1.setDefault(False)
        self.ZBE_V2.setDefault(False)
        self.ZBE_S1.setDefault(False)
        self.ZBE_S2.setDefault(False)
        self.ZBE_k1.setDefault(False)
        self.ZBE_k2.setDefault(False)
        self.ZBE_L1.setDefault(False)
        self.ZBE_L2.setDefault(False)
        self.ZBE_V3.setDefault(False)
        self.ZBE_fik_S.setDefault(False)
        self.ZBE_zr_do_st_odH.setDefault(False)
        self.ZBE_k1S.setDefault(False)
        self.ZBE_zr_zo_st_odH.setDefault(False)
        self.ZBE_trat_suhlas_doR.setDefault(False)
        self.ZBE_zr_do_st_odL.setDefault(False)
        self.ZBE_zr_zo_st_odL.setDefault(False)
        self.ZBE_BL.setDefault(False)
        self.ZBE_trat_suhlas_doL.setDefault(False)
        self.ZBE_k2BL.setDefault(False)
        self.ZBE_fik_BL.setDefault(False)
        self.ZBE_HLO_TU1_1.setDefault(False)
        self.ZBE_S.setDefault(False)
        self.ZBE_trat_suhlas_doH.setDefault(False)
        self.RAD_ZBE_fik_28.setDefault(False)
        self.HLO_fiktL.setDefault(False)
        self.RAD_ZBE_TU3.setDefault(False)
        self.RAD_ZBE_39.setDefault(False)
        self.RAD_ZBE_40.setDefault(False)
        self.ZBE_HLO_TU2_a.setDefault(False)
        self.ZBE_HLO_So.setDefault(False)
        self.ZBE_HLO_Lo.setDefault(False)
        self.ZBE_HLO_TU2_b.setDefault(False)
        self.ZBE_HLO_priec.setDefault(False)
        self.LUZ_ZBE_TU1.setDefault(False)
        self.LUZ_fik_BS.setDefault(False)

        QMetaObject.connectSlotsByName(ILTIS)

    # setupUi

    def retranslateUi(self, ILTIS):
        ILTIS.setWindowTitle(QCoreApplication.translate("ILTIS", "App", None))
        self.actionVlastnosti.setText(
            QCoreApplication.translate("ILTIS", "Vlastnosti ...", None)
        )
        self.actionVo_ba_rozsahu_inform_ci.setText(
            QCoreApplication.translate(
                "ILTIS", "Vo\u013eba rozsahu inform\u00e1ci\u00ed", None
            )
        )
        self.actionAlarm_vypn.setText(
            QCoreApplication.translate("ILTIS", "Alarm vypn\u00fa\u0165", None)
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
        self.actionHorizont_lne.setText(
            QCoreApplication.translate("ILTIS", "Horizont\u00e1lne", None)
        )
        self.actionVertik_lne.setText(
            QCoreApplication.translate("ILTIS", "Vertik\u00e1lne", None)
        )
        self.actionVo_ba_profilu.setText(
            QCoreApplication.translate("ILTIS", "Vo\u013eba profilu ...", None)
        )
        self.actionNastavenie_zvuku.setText(
            QCoreApplication.translate("ILTIS", "Nastavenie zvuku ...", None)
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
        self.action_dr_ba.setText(
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
        self.actionRozsah_nform_ci.setText(
            QCoreApplication.translate("ILTIS", "Rozsah nform\u00e1ci\u00ed ...", None)
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
        self.RAD_ZBE_TU4.setText("")
        self.ZBE_L.setText("")
        self.ZBE_fik_L.setText("")
        self.ZBE_zr_zo_st_odR.setText("")
        self.ZBE_k1L.setText("")
        self.ZBE_zr_do_st_odR.setText("")
        self.ZBE_V1.setText("")
        self.ZBE_V2.setText("")
        self.ZBE_S1.setText("")
        self.ZBE_S2.setText("")
        self.ZBE_k1.setText("")
        self.ZBE_k2.setText("")
        self.ZBE_L1.setText("")
        self.ZBE_L2.setText("")
        self.ZBE_V3.setText("")
        self.ZBE_fik_S.setText("")
        self.ZBE_zr_do_st_odH.setText("")
        self.ZBE_k1S.setText("")
        self.ZBE_zr_zo_st_odH.setText("")
        self.ZBE_trat_suhlas_doR.setText("")
        self.ZBE_zr_do_st_odL.setText("")
        self.ZBE_zr_zo_st_odL.setText("")
        self.ZBE_BL.setText("")
        self.ZBE_trat_suhlas_doL.setText("")
        self.ZBE_k2BL.setText("")
        self.ZBE_fik_BL.setText("")
        self.textLuzianky.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" color:#d0d0d0;">Lu\u017eianky</span></p></body></html>',
                None,
            )
        )
        self.ZBE_HLO_TU1_1.setText("")
        self.ZBE_S.setText("")
        self.ZBE_trat_suhlas_doH.setText("")
        self.ZBE_dialkove.setText("")
        self.ZBE_ASVC.setText("")
        self.RAD_ZBE_fik_28.setText("")
        self.HLO_fiktL.setText("")
        self.textRadosina.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" color:#d0d0d0;">Rado\u0161ina</span></p><p><br/></p></body></html>',
                None,
            )
        )
        self.textHlohovec.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" color:#d0d0d0;">Hlohovec</span></p></body></html>',
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

        self.combo_ciel_fi.setItemText(0, "")
        self.combo_ciel_fi.setItemText(
            1, QCoreApplication.translate("ILTIS", "POC", None)
        )

        self.combo_fikt.setItemText(0, "")
        self.combo_fikt.setItemText(
            1, QCoreApplication.translate("ILTIS", "ZR JC", None)
        )

        self.combo_ciel_zr.setItemText(0, "")
        self.combo_ciel_zr.setItemText(
            1, QCoreApplication.translate("ILTIS", "POS-K", None)
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

        self.combo_TS_RAD.setItemText(0, "")
        self.combo_TS_RAD.setItemText(
            1, QCoreApplication.translate("ILTIS", "ZUS", None)
        )
        self.combo_TS_RAD.setItemText(
            2, QCoreApplication.translate("ILTIS", "ZR ZUS", None)
        )
        self.combo_TS_RAD.setItemText(
            3, QCoreApplication.translate("ILTIS", "UTS", None)
        )

        self.combo_TS_HLO.setItemText(0, "")
        self.combo_TS_HLO.setItemText(
            1, QCoreApplication.translate("ILTIS", "UTS", None)
        )

        self.combo_TS_LUZ.setItemText(0, "")
        self.combo_TS_LUZ.setItemText(
            1, QCoreApplication.translate("ILTIS", "ZUS", None)
        )
        self.combo_TS_LUZ.setItemText(
            2, QCoreApplication.translate("ILTIS", "ZR ZUS", None)
        )
        self.combo_TS_LUZ.setItemText(
            3, QCoreApplication.translate("ILTIS", "UTS", None)
        )
        self.combo_TS_LUZ.setItemText(
            4, QCoreApplication.translate("ILTIS", "ZR BP", None)
        )

        self.RAD_ZBE_TU3.setText("")
        self.RAD_ZBE_39.setText("")
        self.RAD_ZBE_40.setText("")
        self.ZBE_HLO_TU2_a.setText("")
        self.ZBE_HLO_So.setText("")
        self.ZBE_HLO_Lo.setText("")
        self.ZBE_HLO_TU2_b.setText("")
        self.ZBE_HLO_priec.setText("")
        self.textZbehy.setText(
            QCoreApplication.translate(
                "ILTIS",
                '<html><head/><body><p><span style=" color:#d0d0d0;">Zbehy</span></p><p><br/></p></body></html>',
                None,
            )
        )
        self.combo_oddielove.setItemText(0, "")
        self.combo_oddielove.setItemText(
            1, QCoreApplication.translate("ILTIS", "PN", None)
        )
        self.combo_oddielove.setItemText(
            2, QCoreApplication.translate("ILTIS", "VOLNO", None)
        )
        self.combo_oddielove.setItemText(
            3, QCoreApplication.translate("ILTIS", "STOJ", None)
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
        self.groupCentrala.setTitle(QCoreApplication.translate("ILTIS", "Zbehy", None))
        self.groupSystem.setTitle(
            QCoreApplication.translate("ILTIS", "Syst\u00e9m:", None)
        )
        self.groupPoruchy.setTitle(
            QCoreApplication.translate("ILTIS", "Poruchy:", None)
        )
        self.textChybaESA.setText(
            QCoreApplication.translate(
                "ILTIS",
                "<html><head/><body><p>Strata spojenia s ESA 44</p><p><br/></p></body></html>",
                None,
            )
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
        self.combo_Riadenie.setItemText(0, "")
        self.combo_Riadenie.setItemText(
            1, QCoreApplication.translate("ILTIS", "LOKAL", None)
        )
        self.combo_Riadenie.setItemText(
            2, QCoreApplication.translate("ILTIS", "CENTR", None)
        )

        self.groupPrehlad.setTitle(
            QCoreApplication.translate("ILTIS", "Preh\u013ead", None)
        )
        self.label_4.setText(QCoreApplication.translate("ILTIS", "obsluhy", None))
        self.ButtonClose_1.setText(QCoreApplication.translate("ILTIS", "X", None))
        self.label_5.setText(QCoreApplication.translate("ILTIS", "Verzia 1.1", None))
        self.label_6.setText(QCoreApplication.translate("ILTIS", "ILTIS-N Zbehy", None))
        self.label_7.setText(
            QCoreApplication.translate("ILTIS", "D\u00e1vid Macko", None)
        )
        self.label_8.setText(QCoreApplication.translate("ILTIS", "2024", None))
        self.label_9.setText(
            QCoreApplication.translate("ILTIS", "Pracovisko lok\u00e1lnej", None)
        )
        self.LUZ_ZBE_TU1.setText("")
        self.LUZ_fik_BS.setText("")
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
