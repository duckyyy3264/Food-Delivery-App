import 'package:food_delivery_app/data/services/reflect.dart';
import 'package:food_delivery_app/features/authentication/models/account/profile.dart';
import 'package:food_delivery_app/features/authentication/models/account/setting.dart';
import 'package:food_delivery_app/features/user/order/models/cart.dart';
import 'package:food_delivery_app/utils/helpers/helper_functions.dart';

@reflector
@jsonSerializable
class User {
  final String? id;
  final String? phoneNumber;
  final String? email;
  final bool? isActive;
  final bool? isStaff;
  final bool? isSuperuser;
  final DateTime? dateJoined;
  final DateTime? lastLogin;
  final bool? isOtpVerified;
  final bool? isRegistrationVerified;
  final UserProfile? profile;
  final UserSetting? setting;
  final String? user1Rooms;
  final String? user2Rooms;
  RestaurantCart? restaurantCart;
  final String? restaurantCarts;
  final String? locations;
  final UserLocation? selectedLocation;
  final String? deliverer;
  final String? restaurant;

  User({
    this.id,
    this.phoneNumber,
    this.email,
    this.isActive,
    this.isStaff,
    this.isSuperuser,
    this.dateJoined,
    this.lastLogin,
    this.isOtpVerified,
    this.isRegistrationVerified,
    this.profile,
    this.setting,
    this.user1Rooms,
    this.user2Rooms,
    this.restaurantCart,
    this.restaurantCarts,
    this.locations,
    this.selectedLocation,
    this.deliverer,
    this.restaurant,
  });

  User.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        phoneNumber = json['phone_number'],
        email = json['email'],
        isActive = json['is_active'],
        isStaff = json['is_staff'],
        isSuperuser = json['is_superuser'],
        dateJoined = DateTime.parse(json['date_joined']),
        lastLogin = DateTime.parse(json['last_login']),
        isOtpVerified = json['is_otp_verified'],
        isRegistrationVerified = json['is_registration_verified'],
        profile = (json['profile'] != null) ? UserProfile.fromJson(json['profile']) : null,
        setting = (json['setting'] != null) ? UserSetting.fromJson(json['setting']) : null,
        user1Rooms = json['user1_rooms'],
        user2Rooms = json['user2_rooms'],
        restaurantCart = json['restaurant_cart'] != null ? RestaurantCart.fromJson(json['restaurant_cart']) : null,
        restaurantCarts = json['restaurant_carts'],
        locations = json['locations'],
        selectedLocation = json['selected_locations'] != null ? UserLocation.fromJson(json['selected_locations']) : null,
        deliverer = json['deliverer'],
        restaurant = json['restaurant']
  ;

  Map<String, dynamic> toJson({bool patch = false}) {
    final Map<String, dynamic> data = {
      'id': id,
      'phone_number': phoneNumber,
      'email': email,
      'is_active': isActive,
      'is_staff': isStaff,
      'is_superuser': isSuperuser,
      'date_joined': dateJoined?.toIso8601String(),
      'last_login': lastLogin?.toIso8601String(),
      'is_otp_verified': isOtpVerified,
      'is_registration_verified': isRegistrationVerified,
      'profile': profile?.toJson(patch: patch),
      'setting': setting?.toJson(patch: patch),
    };

    if (patch) {
      data.removeWhere((key, value) => value == null);
    }

    return data;
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class Me extends User {
  Me({
    String? id,
    String? phoneNumber,
    String? email,
    bool? isActive,
    bool? isStaff,
    bool? isSuperuser,
    DateTime? dateJoined,
    DateTime? lastLogin,
    bool? isOtpVerified,
    bool? isRegistrationVerified,
    UserProfile? profile,
    UserSetting? setting,
  }) : super(
    id: id,
    phoneNumber: phoneNumber,
    email: email,
    isActive: isActive,
    isStaff: isStaff,
    isSuperuser: isSuperuser,
    dateJoined: dateJoined,
    lastLogin: lastLogin,
    isOtpVerified: isOtpVerified,
    isRegistrationVerified: isRegistrationVerified,
    profile: profile,
    setting: setting,
  );

  Me.fromJson(Map<String, dynamic> json) : super.fromJson(json);
}

@reflector
@jsonSerializable
class OTP {
  final String? id;
  final String? user;
  final String? code;
  final DateTime? expiredAt;

  OTP({
    required this.id,
    required this.user,
    required this.code,
    required this.expiredAt,
  });

  OTP.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        user = json['user'],
        code = json['code'],
        expiredAt = DateTime.parse(json['expired_at']);

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'user': user,
      'code': code,
      'expired_at': expiredAt?.toIso8601String(),
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class UserLocation {
  final String? id;
  final String? address;
  final double? latitude;
  final double? longitude;
  final String? name;
  final bool isSelected;

  UserLocation({
    this.id,
    this.address,
    this.latitude,
    this.longitude,
    this.name,
    this.isSelected = false,
  });

  UserLocation.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        address = json['address'],
        latitude = json['latitude'] != null ? double.parse(json['latitude']) : null,
        longitude = json['longitude'] != null ? double.parse(json['longitude']) : null,
        name = json['name'],
        isSelected = json['is_selected'] ?? false;

  Map<String, dynamic> toJson({bool patch = false}) {
    final map = {
      'id': id,
      'address': address,
      'latitude': latitude,
      'longitude': longitude,
      'name': name,
      'is_selected': isSelected,
    };

    if (patch) {
      map.removeWhere((key, value) => value == null);
    }

    return map;
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class BasicUser {
  String? id;
  String? phoneNumber;
  String? name;
  String? avatar;

  BasicUser({
    this.id,
    this.phoneNumber,
    this.name,
    this.avatar,
  });

  BasicUser.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        phoneNumber = json['phone_number'],
        name = json['name'],
        avatar = json['avatar'];

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'phone_number': phoneNumber,
      'name': name,
      'avatar': avatar,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}
