public class Binary {
    public static class TreeNode {
        private TreeNode left, right;
        private String data;

        public TreeNode(String data) {
            this.data = data;
        }

        public void setLeft(TreeNode node) {
            left = node;
        }
        public void setRight(TreeNode node) {
            right = node;
        }
        public TreeNode getLeft() {
            return left;
        }
        public TreeNode getRight() {
            return right;
        }
    }

    public static void preOrder(TreeNode node) {
        if (node!=null) {
            System.out.print(node.data+"->");
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    public static void inOrder(TreeNode node) {
        if (node!=null) {
            preOrder(node.left);
            System.out.print(node.data+"->");
            preOrder(node.right);
        }
    }

    public static void postOrder(TreeNode node) {
        if (node!=null) {
            preOrder(node.left);
            preOrder(node.right);
            System.out.print(node.data+"->");
        }
    }

    public static void main(String[] args) {
        TreeNode node = new TreeNode("화사");

        node.left = new TreeNode("솔라");
        node.right = new TreeNode("문별");

        node.left.left = new TreeNode("휘인");
        node.left.right = new TreeNode("쯔위");
        
        node.right.left = new TreeNode("선미");

        System.out.println("--- 전위 ---");
        preOrder(node);
        System.out.println();
        
        System.out.println("--- 중위 ---");
        inOrder(node);
        System.out.println();

        System.out.println("--- 후위 ---");
        postOrder(node);
    }
}