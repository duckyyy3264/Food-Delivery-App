import 'package:flutter/material.dart';
import 'package:food_delivery_app/utils/constants/colors.dart';
import 'package:food_delivery_app/utils/constants/sizes.dart';

class StatusChip extends StatelessWidget {
  final String status;

  const StatusChip({Key? key, required this.status}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Color color;
    switch (status) {
      case 'ACTIVE':
        color = TColor.active;
        break;
      case 'COMPLETED':
        color = TColor.success;
        break;
      case 'CANCELLED':
        color = TColor.cancel;
        break;
      default:
        color = Colors.black;
    }
    return Container(
      padding: EdgeInsets.symmetric(
        vertical: TSize.xs,
        horizontal: TSize.sm
      ),
      decoration: BoxDecoration(
        border: Border.all(
          width: 1,
          color: color,
        ),
        borderRadius: BorderRadius.circular(TSize.lg),
      ),
      child: Text(status, style: TextStyle(color: color)),
    );
  }
}