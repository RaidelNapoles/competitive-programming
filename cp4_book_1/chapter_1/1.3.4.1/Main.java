public class Main {

    @SuppressWarnings("resource")
    public static void main(String[] args) {
        // 1
        // double d = 15.324547327;
        // DecimalFormat f = new DecimalFormat("#.000");
        // String sol = f.format(d).replace(",", ".");
        // System.out.printf("%7s", sol);
        // System.out.printf("%7.3f\n", new Scanner(System.in).nextDouble());

        // 2
        // Integer n = 15;
        // String zeroes = String.join("", Collections.nCopies(n, String.valueOf('0')));
        // DecimalFormat df = new DecimalFormat("#.".concat(zeroes));
        // String sol = df.format(Math.PI).replace(",", ".");
        // System.out.printf("%s", sol);

        // 3
        // LocalDate date = LocalDate.of(2010, 8, 9);
        // System.out.println(date.getDayOfWeek());
        // LocalDate current = LocalDate.now();
        // Long differenceInDays = ChronoUnit.DAYS.between(date, current);
        // System.out.println(differenceInDays);

        // 4
        // Integer[] numbers = { 9, 9, 9, 5, 5, 5, 7, 7, 7, 4, 3, 3, 1127, 1234, 1, 1,
        // 10, 11 };
        // List<Integer> sol =
        // Arrays.stream(numbers).distinct().sorted().collect(Collectors.toList());
        // System.out.println(sol);

        // 9
        // String str = "FF";
        // int X = 16, Y = 2;
        // System.out.println(new BigInteger(str, X).toString(Y));

        // 10
        String input = "line: a70 and z72 will be replaced, aa24 and a872 will not";
        // Pattern pattern = Pattern.compile("\\s+[a-z]\\d{2}\\s+");
        // Matcher matcher = pattern.matcher(input);
        // String sol = matcher.replaceAll(" *** ");
        // System.out.println(sol);
        System.out.println(input.replaceAll("\\s+[a-z][0-9][0-9]\\s+", "***"));

        // 11
        // BigInteger num = new BigInteger("2147483629");
        // Boolean sol = false;
        // if (num.compareTo(BigInteger.ONE) <= 0)
        // sol = false;
        // else if (num.equals(BigInteger.valueOf(2)))
        // sol = true;
        // else if (num.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO))
        // sol = false;
        // else
        // sol = num.isProbablePrime(10);
        // String output = sol ? "Prime" : "Composite";
        // System.out.println(output);

        // 12
        // try {
        // String expression = "3 + (8 - 7.5) * 10 / 5 - (2 + 5 * 7)";
        // ScriptEngineManager manager = new ScriptEngineManager();
        // ScriptEngine engine = manager.getEngineByName("JavaScript");
        // double sol = ((Number) engine.eval(expression)).doubleValue();
        // System.err.println(sol);
        // } catch (ScriptException e) {
        // e.printStackTrace();
        // }

    }
}
