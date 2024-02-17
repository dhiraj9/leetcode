class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        List<String> res = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        for (String domain : cpdomains) {
            String[] split = domain.split("\\s");
            Integer count = Integer.parseInt(split[0]);
            String[] sub = split[1].split("\\.");
            int len = sub.length;
            StringBuilder sb = new StringBuilder();
            for (int i = len - 1; i>= 0; i--) {
                if (i != len - 1)
                    sb.insert(0, ".");
                sb.insert(0, sub[i]);
                map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + count);
            }
        }
        for (Map.Entry<String,Integer> entry : map.entrySet()) {
            res.add(entry.getValue() + " " + entry.getKey());
        }
        return res;
    }
}