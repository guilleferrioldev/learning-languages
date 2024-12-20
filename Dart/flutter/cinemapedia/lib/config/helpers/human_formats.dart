import 'package:intl/intl.dart';

class HumanFormats {
  static String number(double number) {
    return NumberFormat.compactCurrency(
            symbol: '', decimalDigits: 0, locale: 'en')
        .format(number);
  }
}
