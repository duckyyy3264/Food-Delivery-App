import 'package:flutter/material.dart';
import 'package:food_delivery_app/data/services/user_service.dart';
import 'package:food_delivery_app/features/authentication/models/account/user.dart';
import 'package:food_delivery_app/features/user/food/views/detail/food_detail.dart';
import 'package:food_delivery_app/features/user/food/views/more/food_more.dart';
import 'package:food_delivery_app/features/user/food/views/restaurant/restaurant_category.dart';
import 'package:food_delivery_app/features/user/order/views/location/order_location.dart';
import 'package:food_delivery_app/utils/constants/times.dart';
import 'package:food_delivery_app/utils/helpers/helper_functions.dart';
import 'package:get/get.dart';

class HomeController extends GetxController {
  static HomeController get instance => Get.find();

  User? user;
  Rx<bool> isLoading = true.obs;

  @override
  void onInit() {
    super.onInit();
    initialize();
  }

  Future<void> initialize() async {
    isLoading.value = true;
    user = await UserService.getUser();
    await Future.delayed(Duration(milliseconds: TTime.init));
    update();
    $print("RESTAURANT ${user?.restaurant} - DELIVERER: ${user?.deliverer}");
    isLoading.value = false;
  }

  void getToFoodCategory(String category, {bool getOff = false}) {
    if (getOff) {
      Get.off(
            () => RestaurantCategoryView(),
        arguments: {"category": category},
      );
    } else {
      Get.to(
            () => RestaurantCategoryView(),
        arguments: {"category": category},
      );
    }
  }


  void getToOrderLocation() async {
    final result = await Get.to(() => OrderLocationSelectView()) as bool?;
    $print("Updated ${result}");
    if(result == true) {
      await initialize();
    }
  }


  void getToFoodDetail(String id) {
    Get.to(
      () => FoodDetailView(),
      arguments: {
        "id": id
      }
    );
  }

  void getToFoodMore() {
    Get.to(() => FoodMoreView());
  }
}