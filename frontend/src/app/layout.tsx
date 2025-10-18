import "./globals.css";

export const metadata = {
  title: "Thread Genie",
  description: "An API to help get AI generated answers from online threads",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
