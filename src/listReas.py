#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# classify permissions into R, E, A, S manually.

class ListReas:
	def __init__(self):
		self.rList = [
		"android.permission.ACCESS_LOCATION_EXTRA_COMMANDS",
		"android.permission.BLUETOOTH",
		"android.permission.BLUETOOTH_ADMIN",
		"android.permission.INTERNET",
		"android.permission.NFC",
		"android.permission.READ_EXTERNAL_STORAGE",
		"android.permission.READ_SMS",
		"com.android.voicemail.permission.READ_VOICEMAIL",
		"android.permission.RECEIVE_MMS",
		"android.permission.RECEIVE_SMS",
		"android.permission.RECEIVE_WAP_PUSH"]
		self.eList = [
		"com.android.voicemail.permission.ADD_VOICEMAIL",
		"android.permission.CALL_PHONE",
		"android.permission.CHANGE_CONFIGURATION",
		"android.permission.CHANGE_NETWORK_STATE",
		"android.permission.DISABLE_KEYGUARD",
		"android.permission.FLASHLIGHT",
		"com.android.launcher.permission.INSTALL_SHORTCUT",
		"android.permission.KILL_BACKGROUND_PROCESSES",
		"android.permission.MODIFY_AUDIO_SETTINGS",
		"android.permission.PROCESS_OUTGOING_CALLS",
		"android.permission.REORDER_TASKS",
		"android.permission.REQUEST_INSTALL_PACKAGES",
		"android.permission.RESTART_PACKAGES",
		"android.permission.SEND_SMS",
		"com.android.alarm.permission.SET_ALARM",
		"android.permission.SET_TIME_ZONE",
		"android.permission.SET_WALLPAPER",
		"android.permission.SET_WALLPAPER_HINTS",
		"android.permission.TRANSMIT_IR",
		"com.android.launcher.permission.UNINSTALL_SHORTCUT",
		"android.permission.USE_SIP",
		"android.permission.VIBRATE",
		"android.permission.WAKE_LOCK",
		"android.permission.WRITE_CALENDAR",
		"android.permission.WRITE_CALL_LOG",
		"android.permission.WRITE_CONTACTS",
		"android.permission.WRITE_EXTERNAL_STORAGE",
		"android.permission.WRITE_SYNC_SETTINGS",
		"com.android.voicemail.permission.WRITE_VOICEMAIL"]
		self.aList = [
		"android.permission.ACCESS_COARSE_LOCATION",
		"android.permission.ACCESS_FINE_LOCATION",
		"android.permission.BODY_SENSORS",
		"android.permission.CALL_PHONE",
		"android.permission.CAMERA",
		"android.permission.GET_ACCOUNTS",
		"android.permission.GET_ACCOUNTS_PRIVILEGED",
		"android.permission.GET_TASKS",
		"android.permission.PROCESS_OUTGOING_CALLS",
		"android.permission.READ_CALENDAR",
		"android.permission.READ_CALL_LOG",
		"android.permission.READ_CONTACTS",
		"android.permission.READ_EXTERNAL_STORAGE",
		"android.permission.READ_PHONE_STATE",
		"android.permission.READ_SMS",
		"com.android.voicemail.permission.READ_VOICEMAIL",
		"android.permission.RECEIVE_MMS",
		"android.permission.RECEIVE_SMS",
		"android.permission.RECEIVE_WAP_PUSH",
		"android.permission.RECORD_AUDIO",
		"android.permission.USE_FINGERPRINT",
		"android.permission.USE_SIP"]
		self.sList = [
		"com.android.voicemail.permission.ADD_VOICEMAIL",
		"android.permission.BLUETOOTH",
		"android.permission.CALL_PHONE",
		"android.permission.INTERNET",
		"android.permission.NFC",
		"android.permission.PROCESS_OUTGOING_CALLS",
		"android.permission.SEND_SMS",
		"android.permission.TRANSMIT_IR",
		"android.permission.USE_SIP",
		"com.android.voicemail.permission.WRITE_VOICEMAIL"]
	def getRList(self):
		return self.rList
	def getEList(self):
		return self.eList
	def getAList(self):
		return self.aList
	def getSList(self):
		return self.sList
	def getReasList(self):
		reasList = self.rList + self.eList + self.aList + self.sList
		return list(set(reasList))