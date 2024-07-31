
import 'package:food_delivery_app/data/services/reflect.dart';
import 'package:food_delivery_app/utils/helpers/helper_functions.dart';

@reflector
@jsonSerializable
class Message {
  final String? id;
  final String? senderId;
  final String? receiverId;
  final String? messageType;
  final String? content;
  final DateTime? timestamp;
  final bool? readStatus;

  Message({
    this.id,
    this.senderId,
    this.receiverId,
    this.messageType,
    this.content,
    this.timestamp,
    this.readStatus,
  });

  Message.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        senderId = json['sender'],
        receiverId = json['receiver'],
        messageType = json['message_type'],
        content = json['content'],
        timestamp = DateTime.parse(json['timestamp']),
        readStatus = json['read_status'];

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'sender': senderId,
      'receiver': receiverId,
      'message_type': messageType,
      'content': content,
      'timestamp': timestamp?.toIso8601String(),
      'read_status': readStatus,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class ImageMessage {
  final String messageId;
  final String imageUrl;

  ImageMessage({
    required this.messageId,
    required this.imageUrl,
  });

  ImageMessage.fromJson(Map<String, dynamic> json)
      : messageId = json['message'],
        imageUrl = json['image'];

  Map<String, dynamic> toJson() {
    return {
      'message': messageId,
      'image': imageUrl,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class AudioMessage {
  final String messageId;
  final String audioUrl;

  AudioMessage({
    required this.messageId,
    required this.audioUrl,
  });

  AudioMessage.fromJson(Map<String, dynamic> json)
      : messageId = json['message'],
        audioUrl = json['audio'];

  Map<String, dynamic> toJson() {
    return {
      'message': messageId,
      'audio': audioUrl,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}

@reflector
@jsonSerializable
class LocationMessage {
  final String messageId;
  final double latitude;
  final double longitude;

  LocationMessage({
    required this.messageId,
    required this.latitude,
    required this.longitude,
  });

  LocationMessage.fromJson(Map<String, dynamic> json)
      : messageId = json['message'],
        latitude = json['latitude'].toDouble(),
        longitude = json['longitude'].toDouble();

  Map<String, dynamic> toJson() {
    return {
      'message': messageId,
      'latitude': latitude,
      'longitude': longitude,
    };
  }

  @override
  String toString() {
    return THelperFunction.formatToString(this);
  }
}