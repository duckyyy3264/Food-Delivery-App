import 'package:food_delivery_app/data/services/reflect.dart';
import 'package:food_delivery_app/features/authentication/models/account/user.dart';
import 'package:food_delivery_app/utils/helpers/helper_functions.dart';

@reflector
@jsonSerializable
class UserSetting {
  final String? user;
  final bool? notification;
  final bool? darkMode;
  final bool? sound;
  final bool? automaticallyUpdated;
  final String? language;

  UserSetting({
    this.user,
    this.notification,
    this.darkMode,
    this.sound,
    this.automaticallyUpdated,
    this.language,
  });

  UserSetting.fromJson(Map<String, dynamic> json)
      : user = json['user'],
        notification = json['notification'],
        darkMode = json['dark_mode'],
        sound = json['sound'],
        automaticallyUpdated = json['automatically_updated'],
        language = json['language'];

  Map<String, dynamic> toJson() {
    return {
      'notification': notification,
      'dark_mode': darkMode,
      'sound': sound,
      'automatically_updated': automaticallyUpdated,
      'language': language,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class UserSecuritySetting {
  final UserSetting? setting;
  final bool? faceId;
  final bool? touchId;
  final bool? pinSecurity;

  UserSecuritySetting({
    required this.setting,
    required this.faceId,
    required this.touchId,
    required this.pinSecurity,
  });

  UserSecuritySetting.fromJson(Map<String, dynamic> json)
      : setting = UserSetting.fromJson(json['setting']),
        faceId = json['face_id'],
        touchId = json['touch_id'],
        pinSecurity = json['pin_security'];

  Map<String, dynamic> toJson() {
    return {
      'setting': setting?.toJson(),
      'face_id': faceId,
      'touch_id': touchId,
      'pin_security': pinSecurity,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}