import 'package:flutter/material.dart';
import 'package:food_delivery_app/common/widgets/app_bar/app_bar.dart';
import 'package:food_delivery_app/features/deliverer/registration/controllers/first/registration_first_step_controller.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/first/widgets/registration_operation_info.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/first/widgets/registration_basic_info.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/first/widgets/registration_driver_license.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/first/widgets/registration_emergency_contact.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/first/widgets/registration_other_info.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/first/widgets/registration_residency_info.dart';
import 'package:food_delivery_app/features/deliverer/registration/views/skeleton/registration_skeleton.dart';
import 'package:get/get.dart';

class RegistrationFirstStepView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GetBuilder<RegistrationFirstStepController>(
      init: RegistrationFirstStepController(),
      builder: (controller) {
        return Scaffold(
          appBar: CAppBar(
            title: "Nộp giấy tờ",
            bottom: TabBar(
              controller: controller.tabController,
              // physics: NeverScrollableScrollPhysics(),
              isScrollable: true,
              tabAlignment: TabAlignment.start,
              tabs: [
                Tab(child: Text("Thông tin cơ bản", style: Get.textTheme.bodyMedium)),
                Tab(child: Text("Thông tin cư trú", style: Get.textTheme.bodyMedium)),
                Tab(child: Text("Thông tin hoạt động", style: Get.textTheme.bodyMedium)),
                Tab(child: Text("Lien he khan cap", style: Get.textTheme.bodyMedium)),
                Tab(child: Text("Bang lai & phuong tien", style: Get.textTheme.bodyMedium)),
                Tab(child: Text("Thong tin khac", style: Get.textTheme.bodyMedium)),
              ],
            ),
          ),
          body: Obx(() => TabBarView(
            controller: controller.tabController,
            // physics: NeverScrollableScrollPhysics(),
            children: [
              controller.isLoading.value ? RegistrationSkeleton() : RegistrationBasicInfo(),
              controller.isLoading.value ? RegistrationSkeleton() : RegistrationResidencyInfo(),
              controller.isLoading.value ? RegistrationSkeleton() : RegistrationOperationInfo(),
              controller.isLoading.value ? RegistrationSkeleton() : RegistrationEmergencyContact(),
              controller.isLoading.value ? RegistrationSkeleton() : RegistrationDriverLicense(),
              controller.isLoading.value ? RegistrationSkeleton() : RegistrationOtherInfo(),
            ],
          )),
        );
      },
    );
  }
}