class Solution {
    private class AtomCount {
        public String atom;
        public int count;

        public AtomCount(String atom, int count) {
            this.atom = atom;
            this.count = count;
        }

        public boolean isParentheses() {
            return atom.equals("(");
        }
    }

    private String getCount(String formula, int idx) {
        StringBuilder sb = new StringBuilder();
        sb.append(formula.charAt(idx));
        int endIdx = idx + 1;
        while (endIdx < formula.length()) {
            char c = formula.charAt(endIdx);
            if (!Character.isDigit(c)) break;
            sb.append(c);
            ++endIdx;
        }
        return sb.toString();
    }

    private String getAtom(String formula, int idx) {
        StringBuilder sb = new StringBuilder();
        sb.append(formula.charAt(idx));
        int endIdx = idx + 1;
        while (endIdx < formula.length()) {
            char c = formula.charAt(endIdx);
            if (!Character.isAlphabetic(c)) break;
            if (Character.isUpperCase(c)) break;
            sb.append(c);
            ++endIdx;
        }
        return sb.toString();
    }

    private String stackToString(Stack<AtomCount> stack) {
        TreeMap<String, Integer> map = new TreeMap<>();
        while (!stack.empty()) {
            AtomCount item = stack.pop();
            map.put(item.atom, map.getOrDefault(item.atom, 0) + item.count);
        }
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            sb.append(entry.getKey());
            if (entry.getValue() == 1) continue;
            sb.append(Integer.toString(entry.getValue()));
        }
        return sb.toString();
    }
    public String countOfAtoms(String formula) {
        Stack<AtomCount> stack = new Stack<>();
        int idx = 0;
        while (idx < formula.length()) {
            char c = formula.charAt(idx);
            if (c == '(') {
                stack.add(new AtomCount("(", 0));
                ++idx;
            } else if (c == ')') {
                List<AtomCount> list = new ArrayList<>();
                while (!stack.empty()) {
                    AtomCount item = stack.pop();
                    if (item.isParentheses()) break;
                    list.add(item);
                }
                ++idx;
                int count = 1;
                if (idx < formula.length() && Character.isDigit(formula.charAt(idx))) {
                    String countStr = getCount(formula, idx);
                    idx += countStr.length();
                    count = Integer.parseInt(countStr);
                }
                for (AtomCount item : list) {
                    item.count *= count;
                    stack.add(item);
                }
            } else {
                String atom = getAtom(formula, idx);
                idx += atom.length();
                int count = 1;
                if (idx < formula.length() && Character.isDigit(formula.charAt(idx))) {
                    String countStr = getCount(formula, idx);
                    idx += countStr.length();
                    count = Integer.parseInt(countStr);
                }
                stack.add(new AtomCount(atom, count));
            }
        }
        return stackToString(stack);
    }
}