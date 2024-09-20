import 'package:flutter/material.dart';
import 'package:food_delivery_app/common/widgets/registration/registration_bottom_navigation_bar.dart';
import 'package:food_delivery_app/common/widgets/registration/registration_document_field.dart';
import 'package:food_delivery_app/common/widgets/registration/registration_text_field.dart';
import 'package:food_delivery_app/common/widgets/registration/registration_type_option.dart';
import 'package:food_delivery_app/features/restaurant/registration/controllers/registration_representative_info.dart';
import 'package:get/get.dart';
import 'package:food_delivery_app/utils/constants/sizes.dart';

class RegistrationRepresentativeInfo extends StatefulWidget {
  @override
  State<RegistrationRepresentativeInfo> createState() => _RegistrationRepresentativeInfoState();
}

class _RegistrationRepresentativeInfoState extends State<RegistrationRepresentativeInfo> {

  final controller = Get.put(RegistrationRepresentativeInfoController());

  String selectedRegister = "Cá nhân";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(TSize.spaceBetweenItemsVertical),
        child: ListView(
          children: [
            RegistrationTypeOption(
              label: 'Đăng ký dưới danh nghĩa:',
              types: ['Cá nhân', 'Công ty/Chuỗi'],
              selectedType: selectedRegister,
              onChanged: (newType) {
                setState(() {
                  selectedRegister = newType;
                });
              },
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationTextField(
              label: 'Tên đầy đủ người đại diện',
              controller: controller.fullNameController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationTextField(
              label: 'Email',
              controller: controller.emailController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationTextField(
              label: 'Số điện thoại',
              controller: controller.phoneController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationTextField(
              label: 'Số CMND',
              controller: controller.idNumberController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationDocumentField(
              label: "Ảnh chụp mặt trước CMND",
              controller: controller.frontIdController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationDocumentField(
              label: "Ảnh chụp mặt sau CMND",
              controller: controller.backIdController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationDocumentField(
              label: "Đăng ký kinh doanh",
              controller: controller.businessLicenseController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),

            RegistrationTextField(
              label: 'Mã số thuế',
              controller: controller.taxCodeController,
            ),
            SizedBox(height: TSize.spaceBetweenItemsVertical),
          ],
        ),
      ),
      bottomNavigationBar: RegistrationBottomNavigationBar(
        onSave: () {
          // Implement save logic
        },
        onContinue: () {
          // Implement continue logic
        },
      ),
    );
  }
}
